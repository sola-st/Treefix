# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_reindex.py
# https://github.com/pandas-dev/pandas/issues/42921
if using_array_manager:
    pytest.skip("Array manager does not promote dtype, hence we fail")

if dtype == "timedelta64[ns]" and fill_value == Timedelta(0):
    # use the scalar that is not compatible with the dtype for this test
    fill_value = Timestamp(0)

ser = Series([NaT], dtype=dtype)

result = ser.reindex([0, 1], fill_value=fill_value)
expected = Series([None, fill_value], index=[0, 1], dtype=object)
tm.assert_series_equal(result, expected)
