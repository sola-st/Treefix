# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/cwise_ops_unary_test.py
if grad_rtol is None:
    grad_rtol = _default_tolerance(x.dtype)
if grad_atol is None:
    grad_atol = _default_tolerance(x.dtype)
np_ans = np_func(x)
with self.cached_session(use_gpu=False):
    inx = ops.convert_to_tensor(x)
    y = tf_func(inx)
    tf_cpu = self.evaluate(y)
    self.assertShapeEqual(np_ans, y)
    if x.dtype == np.float16:
        self.assertAllClose(np_ans, tf_cpu, rtol=1e-3, atol=1e-3)
    elif x.dtype == dtypes_lib.bfloat16.as_numpy_dtype:
        self.assertAllClose(np_ans, tf_cpu, rtol=1e-2, atol=1e-2)
    else:
        self.assertAllClose(np_ans, tf_cpu)

    if x.dtype in (np.complex64, np.complex128) and tf_func == math_ops.sign:
        exit()  # Return early

    if x.dtype in (np.float16, dtypes_lib.bfloat16.as_numpy_dtype):
        s = list(np.shape(x))
        jacob_t, _ = gradient_checker.compute_gradient(
            inx, s, y, s, x_init_value=x)
        xf = x.astype(np.float64)
        inxf = ops.convert_to_tensor(xf)
        yf = tf_func(inxf)
        _, jacob_n = gradient_checker.compute_gradient(
            inxf, s, yf, s, x_init_value=xf, delta=1e-2)
        jacob_n = jacob_n.astype(x.dtype)
        self.assertAllClose(jacob_t, jacob_n, rtol=grad_rtol, atol=grad_atol)
    elif x.dtype in (np.float32, np.complex64):
        s = list(np.shape(x))
        jacob_t, jacob_n = gradient_checker.compute_gradient(
            inx, s, y, s, x_init_value=x, delta=1e-3)
        self.assertAllClose(jacob_t, jacob_n, rtol=grad_rtol, atol=grad_atol)
    elif x.dtype in (np.float64, np.complex128):
        s = list(np.shape(x))
        jacob_t, jacob_n = gradient_checker.compute_gradient(
            inx, s, y, s, x_init_value=x, delta=1e-5)
        self.assertAllClose(jacob_t, jacob_n, rtol=grad_rtol, atol=grad_atol)
