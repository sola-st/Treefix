# Extracted from ./data/repos/pandas/pandas/tests/io/xml/test_xml.py
filename = datapath("io", "data", "xml", "books.xml")
with pytest.raises(
    SyntaxError, match=("You have used an incorrect or unsupported XPath")
):
    read_xml(filename, xpath=".//[book]", parser="etree")
