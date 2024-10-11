# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_coercion.py
tdi = pd.timedelta_range("1 Day", periods=4)
cond = np.array([True, False, False, True])

expected = pd.TimedeltaIndex(["1 Day", value, value, "4 Days"])
result = tdi.where(cond, value)
tm.assert_index_equal(result, expected)

# wrong-dtyped NaT
dtnat = np.datetime64("NaT", "ns")
expected = pd.Index([tdi[0], dtnat, dtnat, tdi[3]], dtype=object)
assert expected[1] is dtnat

result = tdi.where(cond, dtnat)
tm.assert_index_equal(result, expected)
