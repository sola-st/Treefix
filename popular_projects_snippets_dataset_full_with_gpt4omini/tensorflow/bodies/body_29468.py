# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/scatter_nd_ops_test.py
with ops.Graph().as_default():
    indices = array_ops.placeholder(dtypes.int32, shape=None)
    updates = array_ops.placeholder(dtypes.int32, shape=None)
    shape = constant_op.constant([0, 3, 2], dtypes.int32)

    with self.cached_session():
        with self.assertRaisesOpError(
            "Indices and updates specified for empty (input|output)"):
            self.scatter_nd(indices, updates, shape).eval(
                feed_dict={
                    indices: np.zeros([2, 2, 2], dtype=np.int32),
                    updates: np.zeros([2, 2, 2], dtype=np.int32)
                })
