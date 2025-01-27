# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/reduction_ops_test.py
self._compare(x, reduction_axes, False, use_gpu=True)
self._compare(x, reduction_axes, False, use_gpu=False)
self._compare(x, reduction_axes, True, use_gpu=True)
self._compare(x, reduction_axes, True, use_gpu=False)
