# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/utils/sitemap.py
from l3.Runtime import _l_
xmlp = lxml.etree.XMLParser(recover=True, remove_comments=True, resolve_entities=False)
_l_(7509)
self._root = lxml.etree.fromstring(xmltext, parser=xmlp)
_l_(7510)
rt = self._root.tag
_l_(7511)
self.type = self._root.tag.split('}', 1)[1] if '}' in rt else rt
_l_(7512)
