# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_rename.py
ser = Series(range(3), index=list("abc"))
for name in ["foo", 123, 123.0, datetime(2001, 11, 11), ("foo",)]:
    ser.rename(name, inplace=True)
    assert ser.name == name

    exp = np.array(["a", "b", "c"], dtype=np.object_)
    tm.assert_numpy_array_equal(ser.index.values, exp)
