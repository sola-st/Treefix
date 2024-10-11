# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_rename.py
ser = Series(range(4), index=list("abcd"))
for name in ["foo", 123, 123.0, datetime(2001, 11, 11), ("foo",)]:
    result = ser.rename(name)
    assert result.name == name
    tm.assert_numpy_array_equal(result.index.values, ser.index.values)
    assert ser.name is None
