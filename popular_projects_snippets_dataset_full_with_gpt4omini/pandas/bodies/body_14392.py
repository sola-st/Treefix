# Extracted from ./data/repos/pandas/pandas/tests/io/pytables/test_round_trip.py

dr = bdate_range("1/1/1940", "1/1/1960")
ts = Series(np.random.randn(len(dr)), index=dr)
try:
    _check_roundtrip(ts, tm.assert_series_equal, path=setup_path)
except OverflowError:
    if is_platform_windows():
        request.node.add_marker(
            pytest.mark.xfail("known failure on some windows platforms")
        )
    raise
