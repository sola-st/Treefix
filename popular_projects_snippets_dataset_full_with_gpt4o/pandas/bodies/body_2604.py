# Extracted from ./data/repos/pandas/pandas/tests/frame/test_block_internals.py
float_frame["E"] = 7.0

expected = float_frame.values.copy()
expected[expected > 1] = 2

float_frame[float_frame > 1] = 2
tm.assert_almost_equal(expected, float_frame.values)
