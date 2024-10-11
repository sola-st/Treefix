# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_grouping.py
# GH16843
# test ensures that index and column keys are recognized correctly
# when number of keys equals axis length of groupby
df = DataFrame(
    [["foo", "bar", "B", 1], ["foo", "bar", "B", 2], ["foo", "baz", "C", 3]],
    columns=["first", "second", "third", "one"],
)
df = df.set_index(["first", "second"])
df = df.groupby(["first", "second", "third"]).size()
assert df.loc[("foo", "bar", "B")] == 2
assert df.loc[("foo", "baz", "C")] == 1
