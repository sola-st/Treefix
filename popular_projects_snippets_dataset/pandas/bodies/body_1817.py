# Extracted from ./data/repos/pandas/pandas/tests/resample/test_resampler_grouper.py
g = test_frame.groupby("A")
r = g.resample("2s")
result = getattr(r, f)(ddof=1)
expected = g.apply(lambda x: getattr(x.resample("2s"), f)(ddof=1))
tm.assert_frame_equal(result, expected)
