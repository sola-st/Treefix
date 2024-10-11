message = 'Invalid syntax in the request payload.' # pragma: no cover

message = 'curl: (6) Could not resolve host: example.com' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/utils/curl.py
from l3.Runtime import _l_
error_msg = f'There was an error parsing the curl command: {message}'
_l_(21139)
raise ValueError(error_msg)
_l_(21140)
