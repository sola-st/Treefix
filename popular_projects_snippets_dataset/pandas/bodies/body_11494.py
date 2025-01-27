# Extracted from ./data/repos/pandas/pandas/tests/io/xml/test_xml.py
filename = datapath("io", "data", "xml", "books.xml")

with pytest.raises(TypeError, match=("is not a valid type for names")):
    read_xml(filename, names="Col1, Col2, Col3", parser=parser)
