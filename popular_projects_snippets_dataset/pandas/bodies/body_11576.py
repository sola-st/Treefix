# Extracted from ./data/repos/pandas/pandas/tests/io/xml/test_to_xml.py
xsl = datapath("io", "data", "xml", "row_field_output.xsl")

with open(xsl, mode) as f:
    xsl_obj = f.read()

output = geom_df.to_xml(stylesheet=xsl_obj)

assert output == xsl_expected
