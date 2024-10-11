# Extracted from ./data/repos/pandas/pandas/tests/frame/test_nonunique_indexes.py
# multiple assignments that change dtypes
# the location indexer is a slice
# GH 6120
df = DataFrame(np.random.randn(5, 2), columns=["that", "that"])
expected = DataFrame(1.0, index=range(5), columns=["that", "that"])

df["that"] = 1.0
check(df, expected)

df = DataFrame(np.random.rand(5, 2), columns=["that", "that"])
expected = DataFrame(1, index=range(5), columns=["that", "that"])

df["that"] = 1
check(df, expected)
