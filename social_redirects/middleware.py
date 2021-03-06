from __future__ import unicode_literals

from django import http
from django.apps import apps
from django.conf import settings
from django.contrib.sites.shortcuts import get_current_site
from django.core.exceptions import ImproperlyConfigured
from django.shortcuts import render
from django.utils.deprecation import MiddlewareMixin

from .models import Redirect

import re


SOCIAL_USER_AGENTS = [
    'slackbot',
    'facebookexternalhit'
]


class RedirectFallbackMiddleware(MiddlewareMixin):
    # Defined as class-level attributes to be subclassing-friendly.
    response_gone_class = http.HttpResponseGone
    response_redirect_class = http.HttpResponsePermanentRedirect

    def __init__(self, get_response=None):
        if not apps.is_installed('django.contrib.sites'):
            raise ImproperlyConfigured(
                "You cannot use RedirectFallbackMiddleware when "
                "django.contrib.sites is not installed."
            )
        super(RedirectFallbackMiddleware, self).__init__(get_response)

    def process_response(self, request, response):

        # No need to check for a redirect for non-404 responses.
        if response.status_code != 404:
            return response

        full_path = request.get_full_path()
        try:
            current_site = get_current_site(request)
        except:
            return response

        r = None
        try:
            r = Redirect.objects.get(site=current_site, old_path=full_path)
        except Redirect.DoesNotExist:
            pass
        if r is None and settings.APPEND_SLASH and not request.path.endswith('/'):
            try:
                r = Redirect.objects.get(
                    site=current_site,
                    old_path=request.get_full_path(force_append_slash=True),
                )
            except Redirect.DoesNotExist:
                pass

        if r is not None:

            if r.new_path == '':
                return self.response_gone_class()

            if 'HTTP_USER_AGENT' in request.META and re.match("|".join(SOCIAL_USER_AGENTS), request.META['HTTP_USER_AGENT'], flags=re.I):
                return render(request, "social_redirect.html", {'redirect': r})

            return self.response_redirect_class(r.new_path)

        # No redirect was found. Return the response.
        return response
