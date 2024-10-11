# Extracted from ./data/repos/pandas/pandas/tests/io/xml/test_to_xml.py
with pytest.raises(
    ImportError, match=("lxml not found, please install or use the etree parser.")
):
    geom_df.to_xml()
