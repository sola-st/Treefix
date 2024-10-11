# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_coercion.py

obj = pd.DatetimeIndex(
    ["2011-01-01", "2011-01-02", "2011-01-03", "2011-01-04"], tz=fill_val.tz
)
assert obj.dtype == exp_dtype

exp = pd.DatetimeIndex(
    ["2011-01-01", fill_val.date(), "2011-01-02", "2011-01-03", "2011-01-04"],
    tz=fill_val.tz,
)
self._assert_insert_conversion(obj, fill_val, exp, exp_dtype)

if fill_val.tz:

    # mismatched tzawareness
    ts = pd.Timestamp("2012-01-01")
    result = obj.insert(1, ts)
    expected = obj.astype(object).insert(1, ts)
    assert expected.dtype == object
    tm.assert_index_equal(result, expected)

    ts = pd.Timestamp("2012-01-01", tz="Asia/Tokyo")
    result = obj.insert(1, ts)
    # once deprecation is enforced:
    expected = obj.insert(1, ts.tz_convert(obj.dtype.tz))
    assert expected.dtype == obj.dtype
    tm.assert_index_equal(result, expected)

else:
    # mismatched tzawareness
    ts = pd.Timestamp("2012-01-01", tz="Asia/Tokyo")
    result = obj.insert(1, ts)
    expected = obj.astype(object).insert(1, ts)
    assert expected.dtype == object
    tm.assert_index_equal(result, expected)

item = 1
result = obj.insert(1, item)
expected = obj.astype(object).insert(1, item)
assert expected[1] == item
assert expected.dtype == object
tm.assert_index_equal(result, expected)
