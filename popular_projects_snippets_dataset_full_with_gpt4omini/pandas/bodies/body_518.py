# Extracted from ./data/repos/pandas/pandas/tests/dtypes/test_dtypes.py
c1 = CategoricalDtype(categories, ordered=ordered)
tm.assert_index_equal(c1.categories, pd.Index(categories))
assert c1.ordered is ordered
