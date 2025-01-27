# Extracted from ./data/repos/pandas/pandas/tests/io/xml/test_to_xml.py
with pytest.raises(LookupError, match=("unknown encoding")):
    geom_df.to_xml(encoding="uft-8", parser=parser)
