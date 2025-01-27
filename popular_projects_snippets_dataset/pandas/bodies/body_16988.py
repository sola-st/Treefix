# Extracted from ./data/repos/pandas/pandas/tests/reshape/concat/test_empty.py
# 39037
df1 = DataFrame({"a": [1, 2, 3], "b": ["a", "b", "c"]})
df2 = DataFrame({"a": [1, 2, 3]})

result = concat([df1[:0], df2[:0]])
assert result["a"].dtype == np.int64
assert result["b"].dtype == np.object_
