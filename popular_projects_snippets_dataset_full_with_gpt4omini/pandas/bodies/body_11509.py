# Extracted from ./data/repos/pandas/pandas/tests/io/xml/test_xml.py
from lxml.etree import XSLTParseError

kml = datapath("io", "data", "xml", "cta_rail_lines.kml")
xsl = datapath("io", "data", "xml", "books.xml")

with pytest.raises(XSLTParseError, match=("document is not a stylesheet")):
    read_xml(kml, stylesheet=xsl)
