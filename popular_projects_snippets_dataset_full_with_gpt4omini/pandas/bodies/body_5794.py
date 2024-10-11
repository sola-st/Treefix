# Extracted from ./data/repos/pandas/pandas/tests/extension/test_arrow.py
# Series.combine for "expected" retains bool[pyarrow] dtype
# While "result" return "boolean" dtype
right = pd.Series(right._values.to_numpy(), dtype="boolean")
super().assert_series_equal(left, right, *args, **kwargs)
