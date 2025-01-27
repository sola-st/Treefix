# Extracted from ./data/repos/pandas/pandas/tests/indexes/test_base.py
# GH 12631
index = Index(list("ABC"), name="xxx")
result = index.take(np.array([1, 0, -1]))
expected = Index(list("BAC"), name="xxx")
tm.assert_index_equal(result, expected)

# fill_value
result = index.take(np.array([1, 0, -1]), fill_value=True)
expected = Index(["B", "A", np.nan], name="xxx")
tm.assert_index_equal(result, expected)

# allow_fill=False
result = index.take(np.array([1, 0, -1]), allow_fill=False, fill_value=True)
expected = Index(["B", "A", "C"], name="xxx")
tm.assert_index_equal(result, expected)
