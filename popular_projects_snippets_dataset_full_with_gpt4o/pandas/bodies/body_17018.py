# Extracted from ./data/repos/pandas/pandas/tests/reshape/concat/test_concat.py
# GH #1406
df = DataFrame(np.random.randn(1, 3), index=["a"])
df2 = DataFrame(np.random.randn(1, 4), index=["b"])

msg = "Values not found in passed level"
with pytest.raises(ValueError, match=msg):
    concat([df, df], keys=["one", "two"], levels=[["foo", "bar", "baz"]])

msg = "Key one not in level"
with pytest.raises(ValueError, match=msg):
    concat([df, df2], keys=["one", "two"], levels=[["foo", "bar", "baz"]])
