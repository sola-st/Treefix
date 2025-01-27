# Extracted from ./data/repos/pandas/pandas/tests/io/xml/test_xml.py
filename = datapath("io", "data", "xml", "books.xml")
with pytest.raises(TypeError, match="list is not a valid type for iterparse"):
    read_xml(
        filename,
        parser=parser,
        iterparse=["category", "title", "year", "author", "price"],
    )
