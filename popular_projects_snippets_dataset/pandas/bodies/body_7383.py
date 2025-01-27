# Extracted from ./data/repos/pandas/pandas/tests/indexes/multi/test_pickle.py
# this is testing for pickle compat
# need an object to create with
with pytest.raises(TypeError, match="Must pass both levels and codes"):
    MultiIndex()
