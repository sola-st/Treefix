# Extracted from ./data/repos/pandas/pandas/tests/io/xml/test_xml.py
filename = datapath("io", "data", "xml", "books.xml")

with pytest.raises(
    ValueError, match=("Values for parser can only be lxml or etree.")
):
    read_xml(filename, parser="bs4")
