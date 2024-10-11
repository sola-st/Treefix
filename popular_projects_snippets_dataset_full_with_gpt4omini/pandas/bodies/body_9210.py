# Extracted from ./data/repos/pandas/pandas/tests/arrays/categorical/test_missing.py
# GH 28384
cat_type = CategoricalDtype(categories)

# !=
result = Series(a1, dtype=cat_type) != Series(a2, dtype=cat_type)
expected = Series(a1) != Series(a2)
tm.assert_series_equal(result, expected)

# ==
result = Series(a1, dtype=cat_type) == Series(a2, dtype=cat_type)
expected = Series(a1) == Series(a2)
tm.assert_series_equal(result, expected)
