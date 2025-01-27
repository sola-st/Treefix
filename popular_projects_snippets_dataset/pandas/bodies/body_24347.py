# Extracted from ./data/repos/pandas/pandas/io/xml.py
children: list[Any]

if self.names:
    if self.iterparse:
        children = self.iterparse[next(iter(self.iterparse))]
    else:
        children = self.xml_doc.xpath(
            self.xpath + "[1]/*", namespaces=self.namespaces
        )

    if is_list_like(self.names):
        if len(self.names) < len(children):
            raise ValueError(
                "names does not match length of child elements in xpath."
            )
    else:
        raise TypeError(
            f"{type(self.names).__name__} is not a valid type for names"
        )
