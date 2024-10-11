# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_set_name.py
ser = Series([1, 2, 3])
ser2 = ser._set_name("foo")
assert ser2.name == "foo"
assert ser.name is None
assert ser is not ser2
