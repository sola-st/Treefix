# Extracted from ./data/repos/pandas/pandas/tests/indexes/categorical/test_category.py
ci = CategoricalIndex([0, 1, 1])
result = ci.insert(0, pd.NaT)
expected = Index([pd.NaT, 0, 1, 1], dtype=object)
tm.assert_index_equal(result, expected)
