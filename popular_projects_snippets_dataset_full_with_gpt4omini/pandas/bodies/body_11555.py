# Extracted from ./data/repos/pandas/pandas/tests/io/xml/test_to_xml.py
with pytest.raises(TypeError, match=("is not a valid type for elem_cols")):
    geom_df.to_xml(elem_cols='"shape", "degree", "sides"', parser=parser)
