# Extracted from ./data/repos/pandas/pandas/io/xml.py
"""
        Notes
        -----
        `etree` supports limited XPath. If user attempts a more complex
        expression syntax error will raise.
        """

msg = (
    "xpath does not return any nodes or attributes. "
    "Be sure to specify in `xpath` the parent nodes of "
    "children and attributes to parse. "
    "If document uses namespaces denoted with "
    "xmlns, be sure to define namespaces and "
    "use them in xpath."
)
try:
    elems = self.xml_doc.findall(self.xpath, namespaces=self.namespaces)
    children = [ch for el in elems for ch in el.findall("*")]
    attrs = {k: v for el in elems for k, v in el.attrib.items()}

    if elems is None:
        raise ValueError(msg)

    if elems is not None:
        if self.elems_only and children == []:
            raise ValueError(msg)
        if self.attrs_only and attrs == {}:
            raise ValueError(msg)
        if children == [] and attrs == {}:
            raise ValueError(msg)

except (KeyError, SyntaxError):
    raise SyntaxError(
        "You have used an incorrect or unsupported XPath "
        "expression for etree library or you used an "
        "undeclared namespace prefix."
    )

exit(elems)
