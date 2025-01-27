# Extracted from ./data/repos/pandas/pandas/tests/test_nanops.py
# GH 42878 bottleneck sometimes produces unreliable results for mean and sum
assert not nanops._bn_ok_dtype(np.dtype(any_real_numpy_dtype).type, func)
