# Extracted from ./data/repos/pandas/pandas/tests/io/pytables/test_select.py

# GH 6169
# recreate multi-indexes when columns is passed
# in the `where` argument
index = MultiIndex(
    levels=[["foo", "bar", "baz", "qux"], ["one", "two", "three"]],
    codes=[[0, 0, 0, 1, 1, 2, 2, 3, 3, 3], [0, 1, 2, 0, 1, 1, 2, 0, 1, 2]],
    names=["foo_name", "bar_name"],
)

# With a DataFrame
df = DataFrame(np.random.randn(10, 3), index=index, columns=["A", "B", "C"])

with ensure_clean_store(setup_path) as store:
    store.put("df", df, format="table")
    expected = df[["A"]]

    tm.assert_frame_equal(store.select("df", columns=["A"]), expected)

    tm.assert_frame_equal(store.select("df", where="columns=['A']"), expected)

# With a Series
s = Series(np.random.randn(10), index=index, name="A")
with ensure_clean_store(setup_path) as store:
    store.put("s", s, format="table")
    tm.assert_series_equal(store.select("s", where="columns=['A']"), s)
