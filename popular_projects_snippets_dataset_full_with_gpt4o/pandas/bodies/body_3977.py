# Extracted from ./data/repos/pandas/pandas/tests/frame/test_api.py
empty_frame = DataFrame()
assert empty_frame.empty

assert not float_frame.empty
assert not float_string_frame.empty

# corner case
df = DataFrame({"A": [1.0, 2.0, 3.0], "B": ["a", "b", "c"]}, index=np.arange(3))
del df["A"]
assert not df.empty
