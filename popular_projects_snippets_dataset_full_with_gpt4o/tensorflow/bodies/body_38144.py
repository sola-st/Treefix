# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/cwise_ops_test.py
with self.cached_session():
    inx = ops.convert_to_tensor(x)
    iny = ops.convert_to_tensor(y)
    out = array_ops.where(c, inx, iny)
    s = list(np.shape(x))
    jacob_t, jacob_n = gradient_checker.compute_gradient(
        iny, s, out, s, x_init_value=y)
    if numeric_gradient_type is not None:
        xf = x.astype(numeric_gradient_type)
        yf = y.astype(numeric_gradient_type)
        inxf = ops.convert_to_tensor(xf)
        inyf = ops.convert_to_tensor(yf)
        outf = array_ops.where(c, inxf, inyf)
        _, jacob_n = gradient_checker.compute_gradient(
            inyf, s, outf, s, x_init_value=yf)
        jacob_n = jacob_n.astype(x.dtype)
if x.dtype == np.float16:
    self.assertAllClose(jacob_t, jacob_n, rtol=1e-3, atol=1e-3)
elif x.dtype == np.float32:
    self.assertAllClose(jacob_t, jacob_n, rtol=1e-3, atol=1e-3)
elif x.dtype == np.float64:
    self.assertAllClose(jacob_t, jacob_n, rtol=1e-5, atol=1e-5)
