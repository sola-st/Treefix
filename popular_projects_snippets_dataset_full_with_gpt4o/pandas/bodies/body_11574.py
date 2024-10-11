# Extracted from ./data/repos/pandas/pandas/tests/io/xml/test_to_xml.py
xsl = datapath("io", "data", "xml", "row_field_output.xsl")

with open(xsl, mode) as f:
    assert geom_df.to_xml(stylesheet=f) == xsl_expected
