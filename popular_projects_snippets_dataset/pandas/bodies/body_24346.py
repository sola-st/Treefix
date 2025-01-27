# Extracted from ./data/repos/pandas/pandas/io/xml.py

msg = (
    "xpath does not return any nodes or attributes. "
    "Be sure to specify in `xpath` the parent nodes of "
    "children and attributes to parse. "
    "If document uses namespaces denoted with "
    "xmlns, be sure to define namespaces and "
    "use them in xpath."
)

elems = self.xml_doc.xpath(self.xpath, namespaces=self.namespaces)
children = [ch for el in elems for ch in el.xpath("*")]
attrs = {k: v for el in elems for k, v in el.attrib.items()}

if elems == []:
    raise ValueError(msg)

if elems != []:
    if self.elems_only and children == []:
        raise ValueError(msg)
    if self.attrs_only and attrs == {}:
        raise ValueError(msg)
    if children == [] and attrs == {}:
        raise ValueError(msg)

exit(elems)
