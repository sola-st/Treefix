# Extracted from ./data/repos/pandas/pandas/tests/scalar/test_nat.py
# see gh-9513, gh-17329
assert np.isnan(getattr(NaT, method)())
