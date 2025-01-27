# Extracted from ./data/repos/tensorflow/tensorflow/python/client/session_partial_run_test.py
a = array_ops.placeholder(dtypes.float32)
b = a * 2.0

h = sess.partial_run_setup(fetches=[b], feeds=[a])
sess.partial_run(h, [], {a: 3.0})
r = sess.partial_run(h, [b], {})
self.assertEqual([6.0], r)
