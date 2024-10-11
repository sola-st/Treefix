# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_scalar_compat.py
dti = DatetimeIndex([pd.NaT, Timestamp("2018-01-01 01:00:00")])
result = dti.normalize()
expected = DatetimeIndex([pd.NaT, Timestamp("2018-01-01")])
tm.assert_index_equal(result, expected)
