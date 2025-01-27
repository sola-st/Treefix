# Extracted from ./data/repos/tensorflow/tensorflow/python/client/session_partial_run_test.py
a = array_ops.placeholder(dtypes.float32, shape=[])
b = array_ops.placeholder(dtypes.float32, shape=[])
c = array_ops.placeholder(dtypes.float32, shape=[])
r1 = math_ops.add(a, b)
r2 = math_ops.multiply(a, c)

h = sess.partial_run_setup([r1, r2], [a, b, c])
sess.partial_run(h, r1, feed_dict={a: 1, b: 2})
with self.assertRaisesRegex(errors.InvalidArgumentError,
                            'has already been fed.$'):
    sess.partial_run(h, r2, feed_dict={a: 1, c: 3})
