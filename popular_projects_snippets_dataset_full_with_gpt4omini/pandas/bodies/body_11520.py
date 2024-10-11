# Extracted from ./data/repos/pandas/pandas/tests/io/xml/test_xml.py
url = "https://www.w3schools.com/xml/books.xml"
with pytest.raises(
    ParserError, match=("iterparse is designed for large XML files")
):
    read_xml(
        url,
        parser=parser,
        iterparse={"row": ["shape", "degrees", "sides", "date"]},
    )
