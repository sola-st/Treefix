# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/special_math_ops_test.py
with self.cached_session():
    r = np.random.RandomState(0)
    inputs = [np.array(r.randn(*shape)) for shape in input_shapes]
    input_tensors = [constant_op.constant(x, shape=x.shape) for x in inputs]
    analytical, numerical = gradient_checker_v2.compute_gradient(
        lambda *xs: special_math_ops.einsum(s, *xs), input_tensors)
    self.assertLess(
        gradient_checker_v2.max_error(analytical, numerical), 1e-4)
