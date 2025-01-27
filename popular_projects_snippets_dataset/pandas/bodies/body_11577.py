# Extracted from ./data/repos/pandas/pandas/tests/io/xml/test_to_xml.py
from lxml.etree import XMLSyntaxError

xsl = os.path.join("data", "xml", "row_field_output.xslt")

with pytest.raises(
    XMLSyntaxError,
    match=("Start tag expected, '<' not found"),
):
    geom_df.to_xml(stylesheet=xsl)
