# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_rename.py

tuples_index = [("foo1", "bar1"), ("foo2", "bar2")]
tuples_columns = [("fizz1", "buzz1"), ("fizz2", "buzz2")]
index = MultiIndex.from_tuples(tuples_index, names=["foo", "bar"])
columns = MultiIndex.from_tuples(tuples_columns, names=["fizz", "buzz"])
df = DataFrame([(0, 0), (1, 1)], index=index, columns=columns)

#
# without specifying level -> across all levels

renamed = df.rename(
    index={"foo1": "foo3", "bar2": "bar3"},
    columns={"fizz1": "fizz3", "buzz2": "buzz3"},
)
new_index = MultiIndex.from_tuples(
    [("foo3", "bar1"), ("foo2", "bar3")], names=["foo", "bar"]
)
new_columns = MultiIndex.from_tuples(
    [("fizz3", "buzz1"), ("fizz2", "buzz3")], names=["fizz", "buzz"]
)
tm.assert_index_equal(renamed.index, new_index)
tm.assert_index_equal(renamed.columns, new_columns)
assert renamed.index.names == df.index.names
assert renamed.columns.names == df.columns.names

#
# with specifying a level (GH13766)

# dict
new_columns = MultiIndex.from_tuples(
    [("fizz3", "buzz1"), ("fizz2", "buzz2")], names=["fizz", "buzz"]
)
renamed = df.rename(columns={"fizz1": "fizz3", "buzz2": "buzz3"}, level=0)
tm.assert_index_equal(renamed.columns, new_columns)
renamed = df.rename(columns={"fizz1": "fizz3", "buzz2": "buzz3"}, level="fizz")
tm.assert_index_equal(renamed.columns, new_columns)

new_columns = MultiIndex.from_tuples(
    [("fizz1", "buzz1"), ("fizz2", "buzz3")], names=["fizz", "buzz"]
)
renamed = df.rename(columns={"fizz1": "fizz3", "buzz2": "buzz3"}, level=1)
tm.assert_index_equal(renamed.columns, new_columns)
renamed = df.rename(columns={"fizz1": "fizz3", "buzz2": "buzz3"}, level="buzz")
tm.assert_index_equal(renamed.columns, new_columns)

# function
func = str.upper
new_columns = MultiIndex.from_tuples(
    [("FIZZ1", "buzz1"), ("FIZZ2", "buzz2")], names=["fizz", "buzz"]
)
renamed = df.rename(columns=func, level=0)
tm.assert_index_equal(renamed.columns, new_columns)
renamed = df.rename(columns=func, level="fizz")
tm.assert_index_equal(renamed.columns, new_columns)

new_columns = MultiIndex.from_tuples(
    [("fizz1", "BUZZ1"), ("fizz2", "BUZZ2")], names=["fizz", "buzz"]
)
renamed = df.rename(columns=func, level=1)
tm.assert_index_equal(renamed.columns, new_columns)
renamed = df.rename(columns=func, level="buzz")
tm.assert_index_equal(renamed.columns, new_columns)

# index
new_index = MultiIndex.from_tuples(
    [("foo3", "bar1"), ("foo2", "bar2")], names=["foo", "bar"]
)
renamed = df.rename(index={"foo1": "foo3", "bar2": "bar3"}, level=0)
tm.assert_index_equal(renamed.index, new_index)
