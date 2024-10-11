# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/broadcast_to_ops_test.py
with self.session():
    x = np.array([b"1", b"2", b"3"])
    v_tf = array_ops.broadcast_to(constant_op.constant(x), [3, 3])
    v_np = np.broadcast_to(x, [3, 3])
    self.assertAllEqual(v_tf, v_np)
