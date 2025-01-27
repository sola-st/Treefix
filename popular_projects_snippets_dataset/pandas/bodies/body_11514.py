# Extracted from ./data/repos/pandas/pandas/tests/io/xml/test_xml.py
kml = datapath("io", "data", "xml", "cta_rail_lines.kml")
xsl = datapath("io", "data", "xml", "flatten_doc.xsl")

xsl_obj: BytesIO | StringIO

with open(xsl, mode) as f:
    if mode == "rb":
        xsl_obj = BytesIO(f.read())
    else:
        xsl_obj = StringIO(f.read())

    read_xml(kml, stylesheet=xsl_obj)

    assert not f.closed
