# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/linkextractors/lxmlhtml.py
from l3.Runtime import _l_
links = [x for x in links if self._link_allowed(x)]
_l_(7503)
if self.canonicalize:
    _l_(7506)

    for link in links:
        _l_(7505)

        link.url = canonicalize_url(link.url)
        _l_(7504)
links = self.link_extractor._process_links(links)
_l_(7507)
aux = links
_l_(7508)
exit(aux)
