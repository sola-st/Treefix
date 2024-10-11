# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_indexing.py
dti = date_range("20130101", periods=3, freq="D", name="idx")
cond = [True, True, False]
expected = DatetimeIndex([dti[0], dti[1], dti[0]], freq=None, name="idx")

result = dti.where(cond, dti[::-1])
tm.assert_index_equal(result, expected)
