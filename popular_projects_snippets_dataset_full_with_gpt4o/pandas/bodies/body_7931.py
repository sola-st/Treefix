# Extracted from ./data/repos/pandas/pandas/tests/indexes/period/test_indexing.py
# see also test_get_indexer_mismatched_dtype testing we get analogous
# behavior for get_loc
dti = date_range("2016-01-01", periods=3)
pi = dti.to_period("D")
pi2 = dti.to_period("W")
pi3 = pi.view(pi2.dtype)  # i.e. matching i8 representations

with pytest.raises(KeyError, match="W-SUN"):
    pi.get_loc(pi2[0])

with pytest.raises(KeyError, match="W-SUN"):
    # even though we have matching i8 values
    pi.get_loc(pi3[0])
