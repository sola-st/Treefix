# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/tape_test.py

def fn(x, y):
    mm, r = two_outputs(x, y)
    exit(r + math_ops.reduce_sum(mm))

a = constant_op.constant([[1., 0.], [0., 1.]])
b = constant_op.constant([[1., 2.], [3., 4.]])
da, db = backprop.gradients_function(fn, [0, 1])(a, b)
with context.graph_mode(), self.cached_session():
    tf_a = constant_op.constant([[1, 0], [0, 1]], dtype=dtypes.float32)
    tf_b = constant_op.constant([[1, 2], [3, 4]], dtype=dtypes.float32)
    tf_mm = math_ops.matmul(tf_a, tf_b)
    tf_rr = 2 * math_ops.reduce_sum(tf_mm)
    tf_da, tf_db = gradients_impl.gradients(tf_rr, [tf_a, tf_b])

    self.assertAllEqual(da, self.evaluate(tf_da))
    self.assertAllEqual(db, self.evaluate(tf_db))
