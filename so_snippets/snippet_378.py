# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/5607551/how-to-urlencode-a-querystring-in-python
from l3.Runtime import _l_
try:
    from six.moves.urllib.parse import urlencode, quote
    _l_(1538)

except ImportError:
    pass
data = {'some': 'query', 'for': 'encoding'}
_l_(1539)
urlencode(data)
_l_(1540)
'some=query&for=encoding'
_l_(1541)
url = '/some/url/with spaces and %;!<>&'
_l_(1542)
quote(url)
_l_(1543)
'/some/url/with%20spaces%20and%20%25%3B%21%3C%3E%26'
_l_(1544)

