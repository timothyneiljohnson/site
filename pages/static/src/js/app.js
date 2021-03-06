window.$ = window.jQuery = require('jquery');
window.ListFuzzySearch = require('./vendor/list.fuzzysearch.min.js');
window.Cookies = window.Cookies = require('js-cookie');
window.smoothScroll = require('smooth-scroll');
window.Groups = require('./groups.js');

var bootstrap = require('bootstrap-sass'),
  List = require('list.js'),
  validator = require('bootstrap-validator');

window.initAutocomplete = function initAutocomplete() {		
  var input = document.getElementById('autocomplete-input');
  
  window.autocomplete = new google.maps.places.Autocomplete(
    /** @type {!HTMLInputElement} */(input),
    {
      types: ['geocode'],
      componentRestrictions: {country: "us"}
    }
  );

  autocomplete.addListener('place_changed', Groups.getAddress);
}
