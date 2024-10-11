# Extracted from ./data/repos/pandas/pandas/tests/frame/test_constructors.py
self._check_basic_constructor(ma.masked_all)

# Check non-masked values
mat = ma.masked_all((2, 3), dtype=float)
mat[0, 0] = 1.0
mat[1, 2] = 2.0
frame = DataFrame(mat, columns=["A", "B", "C"], index=[1, 2])
assert 1.0 == frame["A"][1]
assert 2.0 == frame["C"][2]

# what is this even checking??
mat = ma.masked_all((2, 3), dtype=float)
frame = DataFrame(mat, columns=["A", "B", "C"], index=[1, 2])
assert np.all(~np.asarray(frame == frame))
