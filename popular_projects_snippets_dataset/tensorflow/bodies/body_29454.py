# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/scatter_nd_ops_test.py
if not test.IsBuiltWithCuda():
    exit()
# TODO(simister): Re-enable once binary size increase due to
# scatter_nd ops is under control.
# tf.scatter_nd_mul, tf.scatter_nd_div,
for op in (state_ops.scatter_nd_add, state_ops.scatter_nd_sub,
           state_ops.scatter_nd_update):
    params = np.array([1, 2, 3, 4, 5, 6]).astype(np.float32)
    updates = np.array([-3, -4, -5]).astype(np.float32)
    # With GPU, the code ignores indices that are out of range.
    # We don't test the implementation; just test there's no failures.
    with self.cached_session(force_gpu=True):
        ref = variables.Variable(params)
        self.evaluate(ref.initializer)

        # Indices all in range, no problem.
        indices = np.array([2, 0, 5])
        op(ref, indices, updates).eval()

        # Indices out of range should not fail.
        indices = np.array([-1, 0, 5])
        op(ref, indices, updates).eval()
        indices = np.array([2, 0, 6])
        op(ref, indices, updates).eval()
