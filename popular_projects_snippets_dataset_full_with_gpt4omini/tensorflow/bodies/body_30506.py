# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/broadcast_to_ops_test.py
for input_dim in range(1, 6):
    for output_dim in range(input_dim, 6):
        with self.cached_session():
            input_shape = [2] * input_dim
            output_shape = [2] * output_dim
            x = np.array(np.random.randint(5, size=input_shape), dtype=np.int32)
            v_tf = array_ops.broadcast_to(constant_op.constant(x), output_shape)
            v_np = np.broadcast_to(x, output_shape)
            self.assertAllEqual(v_tf, v_np)
