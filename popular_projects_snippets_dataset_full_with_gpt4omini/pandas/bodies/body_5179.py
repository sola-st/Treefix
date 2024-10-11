# Extracted from ./data/repos/pandas/pandas/tests/scalar/timedelta/test_constructors.py
# GH#8757: test construction with np dtypes
pykwarg, npkwarg = item
expected = np.timedelta64(1, npkwarg).astype("m8[ns]").view("i8")
assert Timedelta(**{pykwarg: npdtype(1)}).value == expected
