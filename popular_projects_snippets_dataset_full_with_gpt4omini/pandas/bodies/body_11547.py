# Extracted from ./data/repos/pandas/pandas/tests/io/xml/test_to_xml.py
output = geom_df.to_xml(na_rep="", parser=parser)
output = equalize_decl(output)

assert output == na_expected
