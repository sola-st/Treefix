# Extracted from ./data/repos/pandas/pandas/tests/io/xml/test_xml.py
from lxml.etree import XMLSyntaxError

kml = os.path.join("data", "xml", "cta_rail_lines.kml")
xsl = os.path.join("data", "xml", "flatten.xsl")

with pytest.raises(
    XMLSyntaxError,
    match=("Start tag expected, '<' not found"),
):
    read_xml(kml, stylesheet=xsl)
