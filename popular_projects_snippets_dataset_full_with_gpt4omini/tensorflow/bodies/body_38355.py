# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/reduction_ops_test.py
if reduction_axes is not None and np.shape(reduction_axes) == (1,):
    # Test scalar reduction_axes argument
    self._compareGradient(x, reduction_axes[0], rtol=rtol, atol=atol)
with self.cached_session():
    t = ops.convert_to_tensor(x)
    su = self._tf_reduce(t, reduction_axes, False)
    jacob_t, jacob_n = gradient_checker.compute_gradient(
        t, x.shape, su, su.get_shape().as_list(), x_init_value=x, delta=1)
self.assertAllClose(jacob_t, jacob_n, rtol=rtol, atol=atol)
