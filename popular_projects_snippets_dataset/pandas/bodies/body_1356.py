# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_iloc.py
# GH#27937
dtype = CategoricalDtype(categories=[not_na])
ser = Series(
    [nulls_fixture, nulls_fixture, nulls_fixture, nulls_fixture], dtype=dtype
)
ser.iloc[:3] = [nulls_fixture, not_na, nulls_fixture]
exp = Series([nulls_fixture, not_na, nulls_fixture, nulls_fixture], dtype=dtype)
tm.assert_series_equal(ser, exp)
