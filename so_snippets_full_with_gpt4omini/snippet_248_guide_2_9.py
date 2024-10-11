import urllib.request # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/2018026/what-are-the-differences-between-the-urllib-urllib2-urllib3-and-requests-modul
from l3.Runtime import _l_
try:
    _l_(612)

    import requests
    _l_(605)
except ImportError:
    _l_(611)

    try:
        _l_(610)

        import urllib.request
        _l_(606)
    except AttributeError:
        _l_(609)

        try:
            import urllib
            _l_(608)

        except ImportError:
            pass


def get_content(url):
    _l_(621)

    try:
        _l_(620)

        aux = requests.get(url).content # Returns requests.models.Response.
        _l_(613) # Returns requests.models.Response.
        return aux # Returns requests.models.Response.
    except NameError:
        _l_(619)

        try:
            _l_(618)

            with urllib.request.urlopen(index_url) as response:
                _l_(615)

                aux = response.read() # Returns http.client.HTTPResponse.
                _l_(614) # Returns http.client.HTTPResponse.
                return aux # Returns http.client.HTTPResponse.
        except AttributeError:
            _l_(617)

            aux = urllib.urlopen(url).read() # Returns an instance.
            _l_(616) # Returns an instance.
            return aux # Returns an instance.

