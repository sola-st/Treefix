# Extracted from ./data/repos/tensorflow/tensorflow/python/client/session_test.py
# Ensure that errors from building the graph get propagated.
data = array_ops.placeholder(dtypes.float32, shape=[])
# pylint: disable=protected-access
enter_1 = gen_control_flow_ops.enter(data, 'foo_1', False)
enter_2 = gen_control_flow_ops.enter(data, 'foo_2', False)
# pylint: enable=protected-access
res = math_ops.add(enter_1, enter_2)
with self.assertRaisesOpError('has inputs from different frames'):
    sess.run(res, feed_dict={data: 1.0})
