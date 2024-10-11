# Extracted from ./data/repos/pandas/pandas/tests/reductions/test_reductions.py
# GH#48378
val = 100_000_000_000_000_000
n_elements = 100
na = np.array([val] * n_elements)
ser = Series([val] * n_elements, dtype="Int64")

result_numpy = np.mean(na)
result_masked = ser.mean()
assert result_masked - result_numpy == 0
assert result_masked == 1e17
