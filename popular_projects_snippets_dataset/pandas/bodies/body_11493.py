# Extracted from ./data/repos/pandas/pandas/tests/io/xml/test_xml.py
filename = datapath("io", "data", "xml", "books.xml")

with pytest.raises(ValueError, match=("names does not match length")):
    read_xml(filename, names=["Col1", "Col2", "Col3"], parser=parser)
