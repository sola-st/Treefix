# Extracted from ./data/repos/pandas/pandas/tests/resample/test_resampler_grouper.py
g = test_frame.groupby("A")

expected = g.B.apply(lambda x: x.resample("2s").mean())

result = g.resample("2s").B.mean()
tm.assert_series_equal(result, expected)

result = g.B.resample("2s").mean()
tm.assert_series_equal(result, expected)

result = g.resample("2s").mean().B
tm.assert_series_equal(result, expected)
