import sys # pragma: no cover

sys.modules.pop('urllib.request', None) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/2792650/import-error-no-module-name-urllib2
from l3.Runtime import _l_
try:
    import urllib.request
    _l_(15094)

except ImportError:
    pass
url = "http://www.google.com/"
_l_(15095)
request = urllib.request.Request(url)
_l_(15096)
response = urllib.request.urlopen(request)
_l_(15097)
print (response.read().decode('utf-8'))
_l_(15098)

