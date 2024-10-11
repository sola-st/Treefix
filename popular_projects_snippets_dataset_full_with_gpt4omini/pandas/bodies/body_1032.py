# Extracted from ./data/repos/pandas/pandas/tests/indexing/multiindex/test_chaining_and_caching.py
# Inplace ops, originally from:
# https://stackoverflow.com/questions/20508968/series-fillna-in-a-multiindex-dataframe-does-not-fill-is-this-a-bug
a = [12, 23]
b = [123, None]
c = [1234, 2345]
d = [12345, 23456]
tuples = [("eyes", "left"), ("eyes", "right"), ("ears", "left"), ("ears", "right")]
events = {
    ("eyes", "left"): a,
    ("eyes", "right"): b,
    ("ears", "left"): c,
    ("ears", "right"): d,
}
multiind = MultiIndex.from_tuples(tuples, names=["part", "side"])
zed = DataFrame(events, index=["a", "b"], columns=multiind)

if using_copy_on_write:
    zed["eyes"]["right"].fillna(value=555, inplace=True)
else:
    msg = "A value is trying to be set on a copy of a slice from a DataFrame"
    with pytest.raises(SettingWithCopyError, match=msg):
        zed["eyes"]["right"].fillna(value=555, inplace=True)
