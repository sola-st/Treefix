# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_values.py
float_frame["foo"] = "bar"

values = float_frame[["A", "B", "C", "D"]].values
assert values.dtype == np.float64
