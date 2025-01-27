# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/sets_test.py
for dtype in _DTYPES:
    self._test_set_union_duplicates_2d(dtype)
