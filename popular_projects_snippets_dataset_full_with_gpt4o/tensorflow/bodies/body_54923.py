# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/smart_cond_test.py
x = array_ops.placeholder(dtype=dtypes.int32, shape=[])
y = constant_op.constant(10)
conditions = [(x > 1, lambda: constant_op.constant(1)),
              (y < 1, raise_exception),
              (False, raise_exception),
              (True, lambda: constant_op.constant(3))]
z = smart_cond.smart_case(conditions, default=raise_exception)
with session.Session() as sess:
    self.assertEqual(sess.run(z, feed_dict={x: 2}), 1)
    self.assertEqual(sess.run(z, feed_dict={x: 0}), 3)
