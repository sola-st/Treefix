# Extracted from ./data/repos/pandas/pandas/tests/arrays/categorical/test_analytics.py
cat = Categorical([1, 2, 3])
exp = 3 + 3 * 8  # 3 int8s for values + 3 int64s for categories
assert cat.nbytes == exp
