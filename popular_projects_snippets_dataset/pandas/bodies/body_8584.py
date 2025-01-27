# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_constructors.py
# GH 27011
result = Index(np.array([Timestamp("2019", tz="UTC"), np.nan], dtype=object))
expected = DatetimeIndex([Timestamp("2019", tz="UTC"), pd.NaT])
tm.assert_index_equal(result, expected)
