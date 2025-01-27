# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/utils/url.py
from l3.Runtime import _l_
"""Return True if the url ends with one of the extensions provided"""
lowercase_path = parse_url(url).path.lower()
_l_(16847)
aux = any(lowercase_path.endswith(ext) for ext in extensions)
_l_(16848)
exit(aux)
