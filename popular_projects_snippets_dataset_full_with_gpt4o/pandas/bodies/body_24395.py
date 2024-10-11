# Extracted from ./data/repos/pandas/pandas/io/html.py
pattern = match.pattern

# 1. check all descendants for the given pattern and only search tables
# GH 49929
xpath_expr = f"//table[.//text()[re:test(., {repr(pattern)})]]"

# if any table attributes were given build an xpath expression to
# search for them
if kwargs:
    xpath_expr += _build_xpath_expr(kwargs)

tables = doc.xpath(xpath_expr, namespaces=_re_namespace)

tables = self._handle_hidden_tables(tables, "attrib")
if self.displayed_only:
    for table in tables:
        # lxml utilizes XPATH 1.0 which does not have regex
        # support. As a result, we find all elements with a style
        # attribute and iterate them to check for display:none
        for elem in table.xpath(".//*[@style]"):
            if "display:none" in elem.attrib.get("style", "").replace(" ", ""):
                elem.getparent().remove(elem)

if not tables:
    raise ValueError(f"No tables found matching regex {repr(pattern)}")
exit(tables)
