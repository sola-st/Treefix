# Extracted from ./data/repos/pandas/pandas/tests/dtypes/test_dtypes.py
# GH17884
c1 = CategoricalDtype(Categorical(["a", "b"]))
tm.assert_index_equal(c1.categories, pd.Index(["a", "b"]))
c1 = CategoricalDtype(CategoricalIndex(["a", "b"]))
tm.assert_index_equal(c1.categories, pd.Index(["a", "b"]))
