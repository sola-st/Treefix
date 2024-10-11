# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_count.py
dm = DataFrame(float_string_frame._series)
df = DataFrame(float_string_frame._series)

tm.assert_series_equal(dm.count(), df.count())
tm.assert_series_equal(dm.count(1), df.count(1))
