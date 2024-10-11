# Extracted from ./data/repos/pandas/pandas/tests/resample/test_base.py
# GH12771 & GH12868

if resample_method == "ohlc" and isinstance(empty_series_dti.index, PeriodIndex):
    request.node.add_marker(
        pytest.mark.xfail(
            reason=f"GH13083: {resample_method} fails for PeriodIndex"
        )
    )

ser = empty_series_dti
result = getattr(ser.resample(freq), resample_method)()

expected = ser.copy()
expected.index = _asfreq_compat(ser.index, freq)

tm.assert_index_equal(result.index, expected.index)
assert result.index.freq == expected.index.freq
tm.assert_series_equal(result, expected, check_dtype=False)
