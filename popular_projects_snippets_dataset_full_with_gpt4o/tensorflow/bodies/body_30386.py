# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/cast_op_test.py
self._testTypes(x, use_gpu=False)
if x.dtype == np.float32 or x.dtype == np.float64:
    self._testTypes(x, use_gpu=True)
