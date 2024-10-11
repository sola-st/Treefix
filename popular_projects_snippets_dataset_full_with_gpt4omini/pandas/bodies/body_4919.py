# Extracted from ./data/repos/pandas/pandas/tests/reductions/test_reductions.py
# GH 15552
tz = tz_aware_fixture
arg = pd.to_datetime(["2019"]).tz_localize(tz)
expected = Series(arg)
result = getattr(np, func)(expected, expected)
tm.assert_series_equal(result, expected)
