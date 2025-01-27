# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_reindex.py
# GH#7774
index = date_range("2013-01-01", periods=3, tz="US/Eastern")
assert str(index.reindex([])[0].tz) == "US/Eastern"
assert str(index.reindex(np.array([]))[0].tz) == "US/Eastern"
