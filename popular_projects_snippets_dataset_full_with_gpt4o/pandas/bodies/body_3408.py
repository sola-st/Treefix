# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_values.py
float_frame.values[:, 0] = 5.0
assert (float_frame.values[:, 0] == 5).all()
