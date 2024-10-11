# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_values.py
values = float_string_frame.values
assert values.shape[1] == len(float_string_frame.columns)
