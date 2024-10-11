# Extracted from ./data/repos/pandas/pandas/tests/series/accessors/test_str_accessor.py
ser = Series(list("abc"))
return_value = ser.drop([0], inplace=True)
assert return_value is None
assert len(ser.str.lower()) == 2
