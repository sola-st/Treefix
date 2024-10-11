# Extracted from ./data/repos/pandas/pandas/tests/io/xml/test_xml.py
kml = os.path.join("data", "xml", "cta_rail_lines.kml")
xsl = os.path.join("data", "xml", "flatten_doc.xsl")

with pytest.raises(
    ValueError, match=("To use stylesheet, you need lxml installed")
):
    read_xml(kml, parser="etree", stylesheet=xsl)
