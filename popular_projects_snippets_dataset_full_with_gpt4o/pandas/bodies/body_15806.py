# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_astype.py
# GH#44414
ser = Series([0, 1, 2, 3])
ser.attrs["Location"] = "Michigan"

result = ser.astype(any_numpy_dtype).attrs
expected = ser.attrs

tm.assert_dict_equal(expected, result)
