# Extracted from ./data/repos/pandas/pandas/tests/io/xml/test_xml_dtypes.py
filename = datapath("io", "data", "xml", "books.xml")
with pytest.raises(TypeError, match=("Type converters must be a dict or subclass")):
    read_xml(filename, converters={"year", str}, parser=parser, iterparse=iterparse)
