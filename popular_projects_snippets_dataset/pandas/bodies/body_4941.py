# Extracted from ./data/repos/pandas/pandas/tests/reductions/test_reductions.py

with pd.option_context("use_bottleneck", use_bottleneck):
    # GH#6915
    # overflowing on the smaller int dtypes
    v = np.arange(5000000, dtype=dtype)
    s = Series(v)

    result = s.sum(skipna=False)
    assert int(result) == v.sum(dtype="int64")
    result = s.min(skipna=False)
    assert int(result) == 0
    result = s.max(skipna=False)
    assert int(result) == v[-1]
