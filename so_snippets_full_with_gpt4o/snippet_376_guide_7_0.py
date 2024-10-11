import json # pragma: no cover
from types import SimpleNamespace # pragma: no cover

class MockResponse: # pragma: no cover
    def json(self): # pragma: no cover
        return {'message': 'Success'} # pragma: no cover
def join_method(self, path): # pragma: no cover
    return SimpleNamespace(get=lambda params=None: MockResponse()) # pragma: no cover
Url = type('Mock', (object,), { # pragma: no cover
    '__init__': lambda self, base_url: setattr(self, 'base_url', base_url), # pragma: no cover
    'join': join_method # pragma: no cover
}) # pragma: no cover

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

