import requests # pragma: no cover

type('Mock', (object,), {'join': lambda self, path: type('Mock', (object,), {'get': lambda self, params: type('Mock', (object,), {'json': lambda: {"data": "example"}})})()}) # pragma: no cover
Url = type('Mock', (object,), {}) # pragma: no cover
api = Url() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/645312/what-is-the-quickest-way-to-http-get-in-python
from l3.Runtime import _l_
try:
    from nap.url import Url
    _l_(14125)

except ImportError:
    pass
api = Url('https://api.github.com')
_l_(14126)

gists = api.join('gists')
_l_(14127)
response = gists.get(params={'since': '2014-05-01T00:00:00Z'})
_l_(14128)
print(response.json())
_l_(14129)

