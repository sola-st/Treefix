# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_reindex.py
# GH 3317, reindexing by both axes loses freq of the index
df = DataFrame(
    np.ones((3, 3)),
    index=[datetime(2012, 1, 1), datetime(2012, 1, 2), datetime(2012, 1, 3)],
    columns=["a", "b", "c"],
)
time_freq = date_range("2012-01-01", "2012-01-03", freq="d")
some_cols = ["a", "b"]

index_freq = df.reindex(index=time_freq).index.freq
both_freq = df.reindex(index=time_freq, columns=some_cols).index.freq
seq_freq = df.reindex(index=time_freq).reindex(columns=some_cols).index.freq
assert index_freq == both_freq
assert index_freq == seq_freq
