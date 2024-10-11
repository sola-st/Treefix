import urllib.request # pragma: no cover
class Mock: pass # pragma: no cover

Mock.urlopen = lambda request: type('MockResponse', (object,), {'read': lambda self: b'<html></html>', '__init__': lambda s: None})() # pragma: no cover
Mock.Request = urllib.request.Request # pragma: no cover
urllib = type('Mock', (object,), {'request': Mock}) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/2792650/import-error-no-module-name-urllib2
from l3.Runtime import _l_
try:
    import urllib.request
    _l_(2598)

except ImportError:
    pass
url = "http://www.google.com/"
_l_(2599)
request = urllib.request.Request(url)
_l_(2600)
response = urllib.request.urlopen(request)
_l_(2601)
print (response.read().decode('utf-8'))
_l_(2602)

