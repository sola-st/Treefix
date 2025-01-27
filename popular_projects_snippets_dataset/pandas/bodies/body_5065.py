# Extracted from ./data/repos/pandas/pandas/tests/scalar/test_nat.py
# see gh-8254, gh-9513, gh-17329
assert getattr(NaT, method)() is NaT
