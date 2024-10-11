# Extracted from ./data/repos/pandas/pandas/tests/reductions/test_reductions.py
with pd.option_context("use_bottleneck", use_bottleneck):
    v = np.arange(5000000, dtype=dtype)
    s = Series(v)

    result = s.sum(skipna=False)
    assert result == v.sum(dtype=dtype)
    result = s.min(skipna=False)
    assert np.allclose(float(result), 0.0)
    result = s.max(skipna=False)
    assert np.allclose(float(result), v[-1])
