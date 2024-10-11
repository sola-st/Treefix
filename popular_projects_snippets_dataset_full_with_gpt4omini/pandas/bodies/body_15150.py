# Extracted from ./data/repos/pandas/pandas/tests/series/test_repr.py
# tidy repr
ser = Series(np.random.randn(arg), name=0)
rep_str = repr(ser)
assert "Name: 0" in rep_str
