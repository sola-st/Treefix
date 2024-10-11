# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_numeric.py
# GH#44772 for the float64 case
box = box_with_array

arr_i8 = np.arange(2 * 10**4).astype(np.int64, copy=False)
arr = arr_i8.astype(dtype, copy=False)
obj = tm.box_expected(arr, box, transpose=False)

expected = arr_i8.view("timedelta64[D]").astype("timedelta64[ns]")
if type(scalar_td) is timedelta:
    expected = expected.astype("timedelta64[us]")

expected = tm.box_expected(expected, box, transpose=False)

result = obj * scalar_td
tm.assert_equal(result, expected)

result = scalar_td * obj
tm.assert_equal(result, expected)
