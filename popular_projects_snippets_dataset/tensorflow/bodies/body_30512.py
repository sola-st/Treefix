# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/broadcast_to_ops_test.py
for dtype in [dtypes.int32, dtypes.int64]:
    with self.cached_session():
        x = np.array([1, 2, 3])
        v_tf = array_ops.broadcast_to(
            constant_op.constant(x), constant_op.constant([3, 3], dtype=dtype))
        shape = v_tf.get_shape().as_list()
        v_np = np.broadcast_to(x, [3, 3])
        self.assertAllEqual(v_tf, v_np)
        # check shape inference when shape input is constant
        self.assertAllEqual(shape, v_np.shape)
