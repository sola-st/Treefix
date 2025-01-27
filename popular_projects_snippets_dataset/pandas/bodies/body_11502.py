# Extracted from ./data/repos/pandas/pandas/tests/io/xml/test_xml.py
filename = datapath("io", "data", "xml", "books.xml")

with pytest.raises(
    ImportError, match=("lxml not found, please install or use the etree parser.")
):
    read_xml(filename)
