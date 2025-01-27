# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_first_valid_index.py
# GH#17400: no valid entries
index = index_func(30)
frame = DataFrame(np.nan, columns=["foo"], index=index)

assert frame.last_valid_index() is None
assert frame.first_valid_index() is None

ser = frame["foo"]
assert ser.first_valid_index() is None
assert ser.last_valid_index() is None
