# Extracted from ./data/repos/pandas/pandas/tests/extension/base/methods.py
# GH 25439
result = nargsort(data_missing_for_sorting, na_position=na_position)
tm.assert_numpy_array_equal(result, expected)
