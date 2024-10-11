# Extracted from ./data/repos/pandas/pandas/tests/apply/test_frame_apply.py
with np.errstate(all="ignore"):
    # ufunc
    result = np.sqrt(float_frame["A"])
    expected = float_frame.apply(np.sqrt)["A"]
    tm.assert_series_equal(result, expected)

    # aggregator
    result = float_frame.apply(np.mean)["A"]
    expected = np.mean(float_frame["A"])
    assert result == expected

    d = float_frame.index[0]
    result = float_frame.apply(np.mean, axis=1)
    expected = np.mean(float_frame.xs(d))
    assert result[d] == expected
    assert result.index is float_frame.index
