# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/cwise_ops_binary_test.py
self._compareCpu(x, y, np_func, tf_func, also_compare_variables)
if x.dtype in (np.float16, np.float32, np.float64, np.complex64,
               np.complex128):
    if tf_func not in (_FLOORDIV, math_ops.floordiv, math_ops.zeta,
                       math_ops.polygamma):
        self._compareGradientX(x, y, np_func, tf_func)
        self._compareGradientY(x, y, np_func, tf_func)
    if tf_func in (math_ops.zeta, math_ops.polygamma):
        # These methods only support gradients in the second parameter
        self._compareGradientY(x, y, np_func, tf_func)
    self._compareGpu(x, y, np_func, tf_func)
