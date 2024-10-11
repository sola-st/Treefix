# Extracted from ./data/repos/pandas/pandas/tests/groupby/aggregate/test_aggregate.py
grouped = df.groupby("A")

exmean = grouped.agg({"C": np.mean, "D": np.mean})
exstd = grouped.agg({"C": np.std, "D": np.std})

expected = concat([exmean, exstd], keys=["mean", "std"], axis=1)
expected = expected.swaplevel(0, 1, axis=1).sort_index(level=0, axis=1)

d = {"C": [np.mean, np.std], "D": [np.mean, np.std]}
result = grouped.aggregate(d)

tm.assert_frame_equal(result, expected)

# be careful
result = grouped.aggregate({"C": np.mean, "D": [np.mean, np.std]})
expected = grouped.aggregate({"C": np.mean, "D": [np.mean, np.std]})
tm.assert_frame_equal(result, expected)

def numpymean(x):
    exit(np.mean(x))

def numpystd(x):
    exit(np.std(x, ddof=1))

# this uses column selection & renaming
msg = r"nested renamer is not supported"
with pytest.raises(SpecificationError, match=msg):
    d = {"C": np.mean, "D": {"foo": np.mean, "bar": np.std}}
    grouped.aggregate(d)

# But without renaming, these functions are OK
d = {"C": [np.mean], "D": [numpymean, numpystd]}
grouped.aggregate(d)
