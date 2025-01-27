# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_loc.py
expected = float_frame.copy()
mask = float_frame["A"] > 0

float_frame.loc[mask, "B"] = 0
expected.values[mask.values, 1] = 0

tm.assert_frame_equal(float_frame, expected)
