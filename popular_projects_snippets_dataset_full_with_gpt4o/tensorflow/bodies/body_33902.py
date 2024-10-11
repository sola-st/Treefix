# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/v1_compat_tests/scatter_nd_ops_test.py
for op in (state_ops.scatter_nd_min, state_ops.scatter_nd_max):
    params = np.array([1, 2, 3, 4, 5, 6]).astype(np.float32)
    updates = np.array([-3, -4, -5]).astype(np.float32)
    with self.cached_session(use_gpu=False):
        ref = variables.VariableV1(params)
        self.evaluate(ref.initializer)

        # Indices all in range, no problem.
        indices = np.array([[2], [0], [5]])
        self.evaluate(op(ref, indices, updates))

        # Test some out of range errors.
        indices = np.array([[-1], [0], [5]])
        with self.assertRaisesOpError(
            r"indices\[0\] = \[-1\] does not index into shape \[6\]"):
            op(ref, indices, updates).eval()

        indices = np.array([[2], [0], [6]])
        with self.assertRaisesOpError(
            r"indices\[2\] = \[6\] does not index into shape \[6\]"):
            op(ref, indices, updates).eval()
