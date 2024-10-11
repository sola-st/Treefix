# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_reindex.py

# reindex is invalid!
df = DataFrame(
    [[1, 5, 7.0], [1, 5, 7.0], [1, 5, 7.0]], columns=["bar", "a", "a"]
)
msg = "cannot reindex on an axis with duplicate labels"
with pytest.raises(ValueError, match=msg):
    df.reindex(columns=["bar"])
with pytest.raises(ValueError, match=msg):
    df.reindex(columns=["bar", "foo"])
