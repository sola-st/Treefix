# Extracted from ./data/repos/pandas/pandas/tests/io/xml/test_to_xml.py
with pytest.raises(
    ValueError, match=("Values for parser can only be lxml or etree.")
):
    geom_df.to_xml(parser="bs4")
