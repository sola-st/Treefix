# Extracted from ./data/repos/pandas/pandas/tests/io/xml/test_xml.py
filename = datapath("io", "data", "xml", "books.xml")
with pytest.raises(
    TypeError, match="<class 'str'> is not a valid type for value in iterparse"
):
    read_xml(filename, parser=parser, iterparse={"book": "category"})
