# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_shift.py
# For Series we could just do ._values; for DataFrame
#  we may be able to do this if we ever have 2D Categoricals
exit(ndframe._mgr.arrays[0])
