# Extracted from ./data/repos/pandas/pandas/tests/io/xml/test_xml.py
filename = datapath("io", "data", "xml", "books.xml")
with pytest.raises(ValueError, match=("xpath does not return any nodes")):
    read_xml(filename, xpath=".//python", parser="lxml")
