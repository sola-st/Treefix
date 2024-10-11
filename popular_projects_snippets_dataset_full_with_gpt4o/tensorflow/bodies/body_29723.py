# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/scatter_ops_test.py
if test.is_gpu_available():
    exit()
for op, _ in _TF_OPS_TO_NUMPY.items():
    params = np.array([1, 2, 3, 4, 5, 6]).astype(np.float32)
    updates = np.array([-3, -4, -5]).astype(np.float32)
    # With GPU, the code ignores indices that are out of range.
    # We don't test the implementation; just test there's no failures.
    with test_util.force_gpu():
        ref = variables.Variable(params)
        self.evaluate(ref.initializer)

        # Indices all in range, no problem.
        indices = np.array([2, 0, 5])
        self.evaluate(op(ref, indices, updates))

        # Indices out of range should not fail.
        indices = np.array([-1, 0, 5])
        self.evaluate(op(ref, indices, updates))
        indices = np.array([2, 0, 6])
        self.evaluate(op(ref, indices, updates))
