# Extracted from ./data/repos/pandas/pandas/tests/frame/indexing/test_insert.py
df = DataFrame(
    np.random.randn(5, 3), index=np.arange(5), columns=["c", "b", "a"]
)

df.insert(0, "foo", df["a"])
tm.assert_index_equal(df.columns, Index(["foo", "c", "b", "a"]))
tm.assert_series_equal(df["a"], df["foo"], check_names=False)

df.insert(2, "bar", df["c"])
tm.assert_index_equal(df.columns, Index(["foo", "c", "bar", "b", "a"]))
tm.assert_almost_equal(df["c"], df["bar"], check_names=False)

with pytest.raises(ValueError, match="already exists"):
    df.insert(1, "a", df["b"])

msg = "cannot insert c, already exists"
with pytest.raises(ValueError, match=msg):
    df.insert(1, "c", df["b"])

df.columns.name = "some_name"
# preserve columns name field
df.insert(0, "baz", df["c"])
assert df.columns.name == "some_name"
