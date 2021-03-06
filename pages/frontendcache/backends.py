from wagtail.contrib.wagtailfrontendcache.backends import BaseBackend, HTTPBackend
import boto.ec2.elb
import boto.ec2.connection
import boto.ec2.instance
import requests
import urlparse


class ElasticLoadBalancedVarnishBackend(BaseBackend):

    def __init__(self, params):
        self.load_balancer_name = params.pop('LOAD_BALANCER_NAME')
        self.profile_name = params.pop('PROFILE_NAME')
        self.region = params.pop('REGION')
        self.port = params.pop('PORT')
        self.hosts = self.get_hosts()
        self.host_names = params.pop('HOST_NAMES')


    def get_hosts(self):
        instances = []
        elb_conn = boto.ec2.elb.connect_to_region(self.region, profile_name=self.profile_name)
        for elb in elb_conn.get_all_load_balancers(load_balancer_names=self.load_balancer_name):
            instances.extend(elb.instances)

        ec2_conn = boto.ec2.connect_to_region(self.region, profile_name=self.profile_name)
        reservations = ec2_conn.get_all_instances([i.id for i in instances])

        hosts = []
        for reservation in reservations:
            for i in reservation.instances:
                hosts.append(i.public_dns_name)

        return hosts


    def purge(self, url):

        for host in self.hosts:
            req = requests.request('PURGE', urlparse.urljoin('http://%s:%s' % (host, self.port), urlparse.urlparse(url).path))
            assert req.status_code == 200

            for host_name in self.host_names:
                req = requests.request('PURGE', urlparse.urljoin('http://%s:%s' % (host, self.port), urlparse.urlparse(url).path), headers={'Host': host_name})
                assert req.status_code == 200



class FastlyBackend(HTTPBackend):
    
    def __init__(self, params):
        self.api_key = params.pop('API_KEY')
        self.hosts = params.pop('HOSTS')


    def purge(self, url):
        for host in self.hosts:
            req = requests.request('PURGE', urlparse.urljoin(host, urlparse.urlparse(url).path), headers={'Fastly-Key': self.api_key})
            assert req.status_code == 200
