# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/5607551/how-to-urlencode-a-querystring-in-python
from l3.Runtime import _l_
try:
    from six.moves.urllib.parse import urlencode, quote
    _l_(13831)

except ImportError:
    pass
data = {'some': 'query', 'for': 'encoding'}
_l_(13832)
urlencode(data)
_l_(13833)
'some=query&for=encoding'
_l_(13834)
url = '/some/url/with spaces and %;!<>&'
_l_(13835)
quote(url)
_l_(13836)
'/some/url/with%20spaces%20and%20%25%3B%21%3C%3E%26'
_l_(13837)

