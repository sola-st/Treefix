# Extracted from ./data/repos/pandas/pandas/tests/indexes/multi/test_get_set.py
frame = multiindex_dataframe_random_data

with pytest.raises(IndexError, match="Too many levels"):
    frame.index._get_level_number(2)
with pytest.raises(IndexError, match="not a valid level number"):
    frame.index._get_level_number(-3)
