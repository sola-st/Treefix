# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_partial.py
# GH 11278
obj = frame_or_series(range(20), index=idx)

expected_value = [3, 7, 11]
expected = frame_or_series(expected_value, expected_idx)

tm.assert_equal(expected, obj.loc[labels])
if frame_or_series is Series:
    tm.assert_series_equal(expected, obj[labels])
