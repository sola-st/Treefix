# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_diff.py
# Combined datetime diff, normal diff and boolean diff test
ts = tm.makeTimeSeries(name="ts")
ts.diff()

# neg n
result = ts.diff(-1)
expected = ts - ts.shift(-1)
tm.assert_series_equal(result, expected)

# 0
result = ts.diff(0)
expected = ts - ts
tm.assert_series_equal(result, expected)
