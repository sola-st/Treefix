# Extracted from ./data/repos/pandas/pandas/tests/io/xml/test_xml.py
with pytest.raises(ParseError, match="no element found"):
    read_xml(val, parser="etree")
