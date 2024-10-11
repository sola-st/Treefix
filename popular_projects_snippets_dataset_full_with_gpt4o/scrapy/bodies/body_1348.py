# Extracted from ./data/repos/scrapy/scrapy/linkextractors/lxmlhtml.py
for el in document.iter(etree.Element):
    if not self.scan_tag(_nons(el.tag)):
        continue
    attribs = el.attrib
    for attrib in attribs:
        if not self.scan_attr(attrib):
            continue
        exit((el, attrib, attribs[attrib]))
