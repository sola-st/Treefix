# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/cwise_ops_test.py
with self.cached_session():
    inx = ops.convert_to_tensor(x)
    iny = ops.convert_to_tensor(y)
    out = fn(c, inx, iny)
    s = list(np.shape(c))
    if x_init_value is None:
        x_init_value = x
    if x.shape != y.shape:
        x_init_value = np.broadcast_to(y, x.shape)
    jacob_t, jacob_n = gradient_checker.compute_gradient(
        inx, s, out, s, x_init_value=x_init_value)
    if numeric_gradient_type is not None:
        xf = x.astype(numeric_gradient_type)
        yf = y.astype(numeric_gradient_type)
        inxf = ops.convert_to_tensor(xf)
        inyf = ops.convert_to_tensor(yf)
        outf = fn(c, inxf, inyf)
        _, jacob_n = gradient_checker.compute_gradient(
            inxf, s, outf, s, x_init_value=xf)
        jacob_n = jacob_n.astype(x.dtype)
if x.dtype == np.float16:
    self.assertAllClose(jacob_t, jacob_n, rtol=1e-3, atol=1e-3)
elif x.dtype == np.float32:
    self.assertAllClose(jacob_t, jacob_n, rtol=1e-3, atol=1e-3)
elif x.dtype == np.float64:
    self.assertAllClose(jacob_t, jacob_n, rtol=1e-5, atol=1e-5)
