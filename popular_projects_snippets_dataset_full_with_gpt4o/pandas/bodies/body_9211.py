# Extracted from ./data/repos/pandas/pandas/tests/arrays/categorical/test_missing.py
# GH#44900
result = Categorical([na_value, na_value])
tm.assert_index_equal(result.categories, Index([], dtype=dtype))
