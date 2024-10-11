import sys # pragma: no cover
import types # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/2018026/what-are-the-differences-between-the-urllib-urllib2-urllib3-and-requests-modul
from l3.Runtime import _l_
try:
    _l_(12076)

    import requests
    _l_(12069)
except ImportError:
    _l_(12075)

    try:
        _l_(12074)

        import urllib.request
        _l_(12070)
    except AttributeError:
        _l_(12073)

        try:
            import urllib
            _l_(12072)

        except ImportError:
            pass


def get_content(url):
    _l_(12085)

    try:
        _l_(12084)

        aux = requests.get(url).content # Returns requests.models.Response.
        _l_(12077) # Returns requests.models.Response.
        return aux # Returns requests.models.Response.
    except NameError:
        _l_(12083)

        try:
            _l_(12082)

            with urllib.request.urlopen(index_url) as response:
                _l_(12079)

                aux = response.read() # Returns http.client.HTTPResponse.
                _l_(12078) # Returns http.client.HTTPResponse.
                return aux # Returns http.client.HTTPResponse.
        except AttributeError:
            _l_(12081)

            aux = urllib.urlopen(url).read() # Returns an instance.
            _l_(12080) # Returns an instance.
            return aux # Returns an instance.

