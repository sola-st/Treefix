# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_rename.py
# GH 46889
ser = Series(["foo", "bar"])
ser_orig = ser.copy()
shallow_copy = ser.rename({1: 9}, copy=False)
ser[0] = "foobar"
if using_copy_on_write:
    assert ser_orig[0] == shallow_copy[0]
    assert ser_orig[1] == shallow_copy[9]
else:
    assert ser[0] == shallow_copy[0]
    assert ser[1] == shallow_copy[9]
