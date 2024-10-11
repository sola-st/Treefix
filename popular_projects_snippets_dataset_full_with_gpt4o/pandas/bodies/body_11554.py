# Extracted from ./data/repos/pandas/pandas/tests/io/xml/test_to_xml.py
with pytest.raises(KeyError, match=("no valid column")):
    geom_df.to_xml(elem_cols=["shape", "degree", "sides"], parser=parser)
