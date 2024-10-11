# Extracted from ./data/repos/pandas/pandas/tests/reshape/concat/test_empty.py
df = DataFrame(columns=list("abc"))
df["a"] = df["a"].astype(np.bool_)
df["b"] = df["b"].astype(np.int32)
df["c"] = df["c"].astype(np.float64)

result = concat([df, df])
assert result["a"].dtype == np.bool_
assert result["b"].dtype == np.int32
assert result["c"].dtype == np.float64

result = concat([df, df.astype(np.float64)])
assert result["a"].dtype == np.object_
assert result["b"].dtype == np.float64
assert result["c"].dtype == np.float64
