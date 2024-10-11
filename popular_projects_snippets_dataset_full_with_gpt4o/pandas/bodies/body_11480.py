# Extracted from ./data/repos/pandas/pandas/tests/io/xml/test_xml.py
filename = datapath("io", "data", "xml", "cta_rail_lines.kml")
with pytest.raises(SyntaxError, match=("you used an undeclared namespace prefix")):
    read_xml(filename, xpath=".//kml:Placemark", parser="etree")
