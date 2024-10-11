# Extracted from ./data/repos/pandas/pandas/tests/io/xml/test_xml_dtypes.py
filename = datapath("io", "data", "xml", "books.xml")
with pytest.raises(
    ValueError, match=('Unable to parse string "Everyday Italian" at position 0')
):
    read_xml(filename, dtype={"title": "Int64"}, parser=parser, iterparse=iterparse)
