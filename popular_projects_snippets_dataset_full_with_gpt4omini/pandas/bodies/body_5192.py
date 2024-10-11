# Extracted from ./data/repos/pandas/pandas/tests/scalar/timedelta/test_constructors.py
# GH#48898
nat = np.timedelta64("NaT", "h")
assert Timedelta(nat) is NaT
