# Extracted from ./data/repos/pandas/pandas/tests/io/xml/test_xml_dtypes.py
filename = datapath("io", "data", "xml", "books.xml")
with pytest.raises(
    TypeError, match=("Only booleans, lists, and dictionaries are accepted")
):
    read_xml(filename, parse_dates={"date"}, parser=parser, iterparse=iterparse)
