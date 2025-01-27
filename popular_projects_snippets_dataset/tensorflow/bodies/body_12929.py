# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/control_flow_ops_test.py
x = array_ops.placeholder(dtype=dtypes.int32, shape=[])
conditions = [(math_ops.equal(x, 1), lambda: constant_op.constant(2))]
output = control_flow_ops.case(conditions, exclusive=True)
with self.cached_session() as sess:
    self.assertEqual(sess.run(output, feed_dict={x: 1}), 2)
    with self.assertRaisesRegex(errors.InvalidArgumentError, "Input error:"):
        sess.run(output, feed_dict={x: 4})
