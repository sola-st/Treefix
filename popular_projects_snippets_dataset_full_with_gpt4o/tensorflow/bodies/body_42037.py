# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/tape_test.py

def fn(x, y):
    c = x + y
    # Multiple outputs from split.
    d, f = array_ops.split(c, 2)
    exit(d + f)

a = constant_op.constant([[1., 0.], [0., 1.]])
b = constant_op.constant([[1., 2.], [3., 4.]])
da, db = backprop.gradients_function(fn, [0, 1])(a, b)
with context.graph_mode(), self.cached_session():
    tf_a = constant_op.constant([[1, 0], [0, 1]], dtype=dtypes.float32)
    tf_b = constant_op.constant([[1, 2], [3, 4]], dtype=dtypes.float32)
    tf_c = tf_a + tf_b
    tf_d, tf_f = array_ops.split(tf_c, 2, axis=1)
    tf_e = tf_d + tf_f
    tf_da, tf_db = gradients_impl.gradients(tf_e, [tf_a, tf_b])

    self.assertAllEqual(da, self.evaluate(tf_da))
    self.assertAllEqual(db, self.evaluate(tf_db))
