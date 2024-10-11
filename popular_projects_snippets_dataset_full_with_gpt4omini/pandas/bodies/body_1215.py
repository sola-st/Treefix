# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_coercion.py
obj = pd.TimedeltaIndex(["1 day", "2 day", "3 day", "4 day"])
assert obj.dtype == "timedelta64[ns]"

# timedelta64 + timedelta64 => timedelta64
exp = pd.TimedeltaIndex(["1 day", "10 day", "2 day", "3 day", "4 day"])
self._assert_insert_conversion(
    obj, pd.Timedelta("10 day"), exp, "timedelta64[ns]"
)

for item in [pd.Timestamp("2012-01-01"), 1]:
    result = obj.insert(1, item)
    expected = obj.astype(object).insert(1, item)
    assert expected.dtype == object
    tm.assert_index_equal(result, expected)
