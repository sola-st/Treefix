# Extracted from ./data/repos/pandas/pandas/tests/arrays/timedeltas/test_reductions.py
tdi = pd.timedelta_range("14 days", periods=6)
tda = tdi._data.reshape(3, 2)

result = tda.mean(axis=0)
expected = tda[1]
tm.assert_timedelta_array_equal(result, expected)

result = tda.mean(axis=1)
expected = tda[:, 0] + Timedelta(hours=12)
tm.assert_timedelta_array_equal(result, expected)

result = tda.mean(axis=None)
expected = tdi.mean()
assert result == expected
