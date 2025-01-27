# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/extensions/httpcache.py
# Use the cached response if the new response is a server error,
# as long as the old response didn't specify must-revalidate.
from l3.Runtime import _l_
if response.status >= 500:
    _l_(17974)

    cc = self._parse_cachecontrol(cachedresponse)
    _l_(17971)
    if b'must-revalidate' not in cc:
        _l_(17973)

        aux = True
        _l_(17972)
        exit(aux)
aux = response.status == 304
_l_(17975)
exit(aux)
