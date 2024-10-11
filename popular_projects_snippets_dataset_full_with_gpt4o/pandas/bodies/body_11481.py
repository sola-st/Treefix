# Extracted from ./data/repos/pandas/pandas/tests/io/xml/test_xml.py
from lxml.etree import XPathEvalError

filename = datapath("io", "data", "xml", "cta_rail_lines.kml")
with pytest.raises(XPathEvalError, match=("Undefined namespace prefix")):
    read_xml(filename, xpath=".//kml:Placemark", parser="lxml")
