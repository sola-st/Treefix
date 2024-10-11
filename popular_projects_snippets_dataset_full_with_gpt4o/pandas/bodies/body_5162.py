# Extracted from ./data/repos/pandas/pandas/tests/scalar/timedelta/test_arithmetic.py
# analogous to GH#15183
td = Timedelta("2 days")
other = Timedelta("3 hours")

arr = np.array([other, td], dtype=object)
res = arr == td
expected = np.array([False, True], dtype=bool)
assert (res == expected).all()

# 2D case
arr = np.array([[other, td], [td, other]], dtype=object)
res = arr != td
expected = np.array([[True, False], [False, True]], dtype=bool)
assert res.shape == expected.shape
assert (res == expected).all()
