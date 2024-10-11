import requests # pragma: no cover
from unittest.mock import MagicMock # pragma: no cover

Url = type('MockUrl', (object,), {'__init__': lambda self, url: None, 'join': lambda self, path: self, 'get': lambda self, params: MagicMock(return_value=MagicMock(json=lambda: {'data': 'mocked data'}))}) # pragma: no cover
api = Url('https://api.github.com') # pragma: no cover
gists = api.join('gists') # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/645312/what-is-the-quickest-way-to-http-get-in-python
from l3.Runtime import _l_
try:
    from nap.url import Url
    _l_(1942)

except ImportError:
    pass
api = Url('https://api.github.com')
_l_(1943)

gists = api.join('gists')
_l_(1944)
response = gists.get(params={'since': '2014-05-01T00:00:00Z'})
_l_(1945)
print(response.json())
_l_(1946)

