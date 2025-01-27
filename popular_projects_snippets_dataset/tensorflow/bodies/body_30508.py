# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/broadcast_to_ops_test.py
input_shape = [2, 1, 3, 2, 2, 2]
output_shape = [1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 15, 3, 2, 2, 2]
with self.cached_session():
    x = np.array(np.random.randint(5, size=input_shape), dtype=np.int32)
    v_tf = array_ops.broadcast_to(constant_op.constant(x), output_shape)
    v_np = np.broadcast_to(x, output_shape)
    self.assertAllEqual(v_tf, v_np)
