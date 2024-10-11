# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/einsum_op_test.py
with self.cached_session():
    r = np.random.RandomState(seed=0)
    for dtype in (np.float32, np.float64, np.complex64, np.complex128):
        with self.subTest(s=s, dtype=dtype):
            tol = 10 * np.sqrt(np.finfo(dtype).resolution)
            if dtype in (np.complex64, np.complex128):
                inputs = [
                    np.array(r.randn(*shape), dtype) +
                    1j * np.array(r.randn(*shape), dtype) for shape in input_shapes
                ]
            else:
                inputs = [
                    np.array(r.randn(*shape), dtype) for shape in input_shapes]
            input_tensors = [
                constant_op.constant(x, shape=x.shape) for x in inputs]
            analytical, numerical = gradient_checker_v2.compute_gradient(
                lambda *xs: gen_linalg_ops.einsum(xs, s), input_tensors)
            self.assertLess(
                gradient_checker_v2.max_error(analytical, numerical), tol)
