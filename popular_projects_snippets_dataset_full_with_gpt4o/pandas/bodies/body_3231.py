# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_first_valid_index.py
N = 30
index = index_func(N)
mat = np.random.randn(N)
mat[:5] = np.nan
mat[-5:] = np.nan

frame = DataFrame({"foo": mat}, index=index)
assert frame.first_valid_index() == frame.index[5]
assert frame.last_valid_index() == frame.index[-6]

ser = frame["foo"]
assert ser.first_valid_index() == frame.index[5]
assert ser.last_valid_index() == frame.index[-6]
