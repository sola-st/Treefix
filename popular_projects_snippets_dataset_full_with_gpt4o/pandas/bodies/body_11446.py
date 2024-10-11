# Extracted from ./data/repos/pandas/pandas/tests/io/xml/test_xml_dtypes.py
filename = datapath("io", "data", "xml", "books.xml")
with pytest.raises(TypeError, match=("'str' object is not callable")):
    read_xml(
        filename, converters={"year": "float"}, parser=parser, iterparse=iterparse
    )
