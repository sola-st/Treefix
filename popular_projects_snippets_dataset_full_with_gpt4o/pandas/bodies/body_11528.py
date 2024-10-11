# Extracted from ./data/repos/pandas/pandas/tests/io/xml/test_xml.py
filename = datapath("io", "data", "xml", "books.xml")
with pytest.raises(
    ParserError, match="No result from selected items in iterparse."
):
    read_xml(
        filename,
        parser=parser,
        iterparse={"node": ["attr1", "elem1", "elem2", "elem3"]},
    )
