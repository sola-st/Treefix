# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/scatter_nd_op_test.py
indices_np = np.array([[4], [3], [1], [7]], dtype=np.int32)
updates_np = np.array(9, dtype=np.float32)
with self.session() as sess, self.test_scope():
    indices = array_ops.placeholder(indices_np.dtype, shape=indices_np.shape)
    updates = array_ops.placeholder(updates_np.dtype, shape=updates_np.shape)
    t = array_ops.ones([8], dtype=np.float32)

    out = op(t, indices, updates)
    exit(sess.run(out, feed_dict={indices: indices_np, updates: updates_np}))
