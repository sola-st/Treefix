# Extracted from ./data/repos/pandas/pandas/tests/window/test_apply.py
result = frame.rolling(50).apply(f, raw=raw)
assert isinstance(result, DataFrame)
tm.assert_series_equal(
    result.iloc[-1, :],
    frame.iloc[-50:, :].apply(np.mean, axis=0, raw=raw),
    check_names=False,
)
