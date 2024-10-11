# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/cwise_ops_binary_test.py
if dtype in (np.complex64, np.complex128):
    x = (1 + np.linspace(0, 2 + 3j, np.prod(xs))).astype(dtype).reshape(xs)
    y = (1 + np.linspace(0, 2 - 2j, np.prod(ys))).astype(dtype).reshape(ys)
else:
    x = (1 + np.linspace(0, 5, np.prod(xs))).astype(dtype).reshape(xs)
    y = (1 + np.linspace(0, 5, np.prod(ys))).astype(dtype).reshape(ys)
self._compareCpu(x, y, np_func, tf_func)
if x.dtype in (np.float16, np.float32, np.float64):
    # TODO(aselle): Make the test work for dtypes:
    #     (np.complex64, np.complex128).
    if tf_func not in (_FLOORDIV, math_ops.floordiv):
        if x.dtype == np.float16:
            # Compare fp16 theoretical gradients to fp32 numerical gradients,
            # since fp16 numerical gradients are too imprecise unless great
            # care is taken with choosing the inputs and the delta. This is
            # a weaker check (in particular, it does not test the op itself,
            # only its gradient), but it's much better than nothing.
            self._compareGradientX(x, y, np_func, tf_func, np.float64)
            self._compareGradientY(x, y, np_func, tf_func, np.float64)
        else:
            self._compareGradientX(x, y, np_func, tf_func)
            self._compareGradientY(x, y, np_func, tf_func)
    self._compareGpu(x, y, np_func, tf_func)
