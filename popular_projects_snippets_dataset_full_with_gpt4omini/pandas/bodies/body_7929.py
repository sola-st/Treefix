# Extracted from ./data/repos/pandas/pandas/tests/indexes/period/test_indexing.py
dti = date_range("2016-01-01", periods=3)
pi = dti.to_period("D")
with pytest.raises(KeyError, match="16801"):
    pi.get_loc(16801)

pi2 = dti.to_period("Y")  # duplicates, ordinals are all 46
with pytest.raises(KeyError, match="46"):
    pi2.get_loc(46)
