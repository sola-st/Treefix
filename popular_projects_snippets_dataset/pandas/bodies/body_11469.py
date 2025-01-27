# Extracted from ./data/repos/pandas/pandas/tests/io/xml/test_xml.py
filename = os.path.join("data", "html", "books.xml")

with pytest.raises(
    ParseError,
    match=("not well-formed"),
):
    read_xml(filename, parser="etree")
