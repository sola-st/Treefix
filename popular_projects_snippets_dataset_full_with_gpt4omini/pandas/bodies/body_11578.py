# Extracted from ./data/repos/pandas/pandas/tests/io/xml/test_to_xml.py
from lxml.etree import XMLSyntaxError

msg = "|".join(
    [
        "Document is empty",
        "Start tag expected, '<' not found",
        # Seen on Mac with lxml 4.9.1
        r"None \(line 0\)",
    ]
)

with pytest.raises(XMLSyntaxError, match=msg):
    geom_df.to_xml(stylesheet=val)
