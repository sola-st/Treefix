# Extracted from ./data/repos/pandas/pandas/tests/io/xml/test_xml.py
from lxml.etree import XMLSyntaxError

msg = "|".join(
    [
        "Document is empty",
        # Seen on Mac with lxml 4.91
        r"None \(line 0\)",
    ]
)
with pytest.raises(XMLSyntaxError, match=msg):
    read_xml(val, parser="lxml")
