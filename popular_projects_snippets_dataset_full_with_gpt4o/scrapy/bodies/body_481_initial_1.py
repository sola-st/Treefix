import lxml.etree # pragma: no cover

lxml = type('Mock', (object,), {'etree': lxml.etree}) # pragma: no cover
self = type('Mock', (object,), {'_root': None, 'type': None})() # pragma: no cover
xmltext = '<root><child>Example</child></root>' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/utils/sitemap.py
from l3.Runtime import _l_
xmlp = lxml.etree.XMLParser(recover=True, remove_comments=True, resolve_entities=False)
_l_(18412)
self._root = lxml.etree.fromstring(xmltext, parser=xmlp)
_l_(18413)
rt = self._root.tag
_l_(18414)
self.type = self._root.tag.split('}', 1)[1] if '}' in rt else rt
_l_(18415)
