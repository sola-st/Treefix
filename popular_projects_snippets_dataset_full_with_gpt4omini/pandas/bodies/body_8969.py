# Extracted from ./data/repos/pandas/pandas/tests/arrays/sparse/test_reductions.py
argmax_result = arr.argmax()
argmin_result = arr.argmin()
assert argmax_result == argmax_expected
assert argmin_result == argmin_expected
