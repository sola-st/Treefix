# Extracted from ./data/repos/pandas/pandas/tests/resample/test_period_index.py
# This is a bug, these should be implemented
# GH 14008
rng = np.arange(len(index), dtype=np.int64)
df = DataFrame(
    {"date": index, "a": rng},
    index=pd.MultiIndex.from_arrays([rng, index], names=["v", "d"]),
)
msg = (
    "Resampling from level= or on= selection with a PeriodIndex is "
    r"not currently supported, use \.set_index\(\.\.\.\) to "
    "explicitly set index"
)
with pytest.raises(NotImplementedError, match=msg):
    df.resample(freq, kind=kind, **kwargs)
