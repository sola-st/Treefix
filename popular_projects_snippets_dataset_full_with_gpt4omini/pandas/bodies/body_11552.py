# Extracted from ./data/repos/pandas/pandas/tests/io/xml/test_to_xml.py
with pytest.raises(TypeError, match=("is not a valid type for attr_cols")):
    geom_df.to_xml(attr_cols='"shape", "degree", "sides"', parser=parser)
