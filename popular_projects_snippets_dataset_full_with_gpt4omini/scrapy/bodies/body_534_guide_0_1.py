from typing import Any # pragma: no cover

message = 'Invalid curl command' # pragma: no cover
error_msg = f'There was an error parsing the curl command: {message}' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/utils/curl.py
from l3.Runtime import _l_
error_msg = f'There was an error parsing the curl command: {message}'
_l_(10023)
raise ValueError(error_msg)
_l_(10024)
