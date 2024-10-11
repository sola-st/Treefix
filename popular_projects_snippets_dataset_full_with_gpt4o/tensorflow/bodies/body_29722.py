# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/scatter_ops_test.py
for op, _ in _TF_OPS_TO_NUMPY.items():
    params = np.array([1, 2, 3, 4, 5, 6]).astype(np.float32)
    updates = np.array([-3, -4, -5]).astype(np.float32)
    if not test.is_gpu_available():
        with self.session(use_gpu=False):
            ref = variables.Variable(params)
            self.evaluate(ref.initializer)

            # Indices all in range, no problem.
            indices = np.array([2, 0, 5])
            self.evaluate(op(ref, indices, updates))

            # Test some out of range errors.
            indices = np.array([-1, 0, 5])
            with self.assertRaisesOpError(
                r'indices\[0\] = -1 is not in \[0, 6\)'):
                self.evaluate(op(ref, indices, updates))

            indices = np.array([2, 0, 6])
            with self.assertRaisesOpError(r'indices\[2\] = 6 is not in \[0, 6\)'):
                self.evaluate(op(ref, indices, updates))
