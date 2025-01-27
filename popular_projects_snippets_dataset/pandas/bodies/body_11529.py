# Extracted from ./data/repos/pandas/pandas/tests/io/xml/test_xml.py
filename = datapath("io", "data", "xml", "books.xml")
with pytest.raises(EmptyDataError, match="No columns to parse from file"):
    read_xml(
        filename,
        parser=parser,
        iterparse={"book": ["attr1", "elem1", "elem2", "elem3"]},
    )
