# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/control_flow_ops_test.py
x = array_ops.placeholder(dtype=dtypes.int32, shape=[])
conditions = [(math_ops.equal(x, 1), lambda: constant_op.constant(2)),
              (math_ops.equal(x, 2), lambda: constant_op.constant(4)),
              (math_ops.equal(x, 2), lambda: constant_op.constant(6))]
default = lambda: constant_op.constant(8)
output = control_flow_ops.case(conditions, default, exclusive=False)
with self.cached_session() as sess:
    self.assertEqual(sess.run(output, feed_dict={x: 1}), 2)
    self.assertEqual(sess.run(output, feed_dict={x: 2}), 4)
    self.assertEqual(sess.run(output, feed_dict={x: 3}), 8)
