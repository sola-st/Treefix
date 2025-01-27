# Extracted from ./data/repos/pandas/pandas/tests/io/test_feather.py

df = pd.DataFrame({"A": [1, 2, 3]})
self.check_round_trip(df)

msg = (
    r"feather does not support serializing .* for the index; "
    r"you can \.reset_index\(\) to make the index into column\(s\)"
)
# non-default index
for index in [
    [2, 3, 4],
    pd.date_range("20130101", periods=3),
    list("abc"),
    [1, 3, 4],
    pd.MultiIndex.from_tuples([("a", 1), ("a", 2), ("b", 1)]),
]:

    df.index = index
    self.check_error_on_write(df, ValueError, msg)

# index with meta-data
df.index = [0, 1, 2]
df.index.name = "foo"
msg = "feather does not serialize index meta-data on a default index"
self.check_error_on_write(df, ValueError, msg)

# column multi-index
df.index = [0, 1, 2]
df.columns = pd.MultiIndex.from_tuples([("a", 1)])
msg = "feather must have string column names"
self.check_error_on_write(df, ValueError, msg)
