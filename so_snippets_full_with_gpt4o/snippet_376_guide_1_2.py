import json # pragma: no cover
from types import SimpleNamespace # pragma: no cover

class Url(SimpleNamespace): # pragma: no cover
    def __init__(self, base_url): # pragma: no cover
        self.base_url = base_url # pragma: no cover
    def join(self, endpoint): # pragma: no cover
        return Url(f'{self.base_url}/{endpoint}') # pragma: no cover
    def get(self, params=None): # pragma: no cover
        class Response: # pragma: no cover
            def json(self): # pragma: no cover
                return {'data': 'example'} # pragma: no cover
        return Response() # pragma: no cover

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

