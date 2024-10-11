# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_period.py
# GH#13043
ser = Series(
    [Period("2015-01-01", freq="D"), Period("2015-01-02", freq="D")],
    name="xxx",
)
assert ser.dtype == "Period[D]"

expected = Series(
    [Period("2015-01-04", freq="D"), Period("2015-01-05", freq="D")],
    name="xxx",
)

obj = tm.box_expected(ser, box_with_array)
if box_with_array is pd.DataFrame:
    assert (obj.dtypes == "Period[D]").all()

expected = tm.box_expected(expected, box_with_array)

result = obj + three_days
tm.assert_equal(result, expected)

result = three_days + obj
tm.assert_equal(result, expected)
