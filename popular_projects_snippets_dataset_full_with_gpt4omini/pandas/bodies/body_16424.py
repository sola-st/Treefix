# Extracted from ./data/repos/pandas/pandas/tests/reshape/test_cut.py
name = "foo"
ser = Series(np.random.randn(100), name=name)

factor = cut(ser, 4)
assert factor.name == name
