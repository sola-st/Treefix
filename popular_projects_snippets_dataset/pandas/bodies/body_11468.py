# Extracted from ./data/repos/pandas/pandas/tests/io/xml/test_xml.py
from lxml.etree import XMLSyntaxError

filename = os.path.join("data", "html", "books.xml")

with pytest.raises(
    XMLSyntaxError,
    match=("Start tag expected, '<' not found"),
):
    read_xml(filename, parser="lxml")
