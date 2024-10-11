# Extracted from ./data/repos/pandas/pandas/tests/indexes/test_subclass.py
# https://github.com/pandas-dev/pandas/issues/47071

idx = CustomIndex([1, 2, 3])
result = idx.insert(0, "string")
expected = Index(["string", 1, 2, 3], dtype=object)
tm.assert_index_equal(result, expected)

df = DataFrame(
    np.random.randn(2, 3), columns=idx, index=Index([1, 2], name="string")
)
result = df.reset_index()
tm.assert_index_equal(result.columns, expected)
