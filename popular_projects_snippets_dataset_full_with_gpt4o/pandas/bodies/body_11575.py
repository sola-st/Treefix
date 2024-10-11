# Extracted from ./data/repos/pandas/pandas/tests/io/xml/test_to_xml.py
xsl_path = datapath("io", "data", "xml", "row_field_output.xsl")

xsl_obj: BytesIO | StringIO

with open(xsl_path, mode) as f:
    if mode == "rb":
        xsl_obj = BytesIO(f.read())
    else:
        xsl_obj = StringIO(f.read())

output = geom_df.to_xml(stylesheet=xsl_obj)

assert output == xsl_expected
