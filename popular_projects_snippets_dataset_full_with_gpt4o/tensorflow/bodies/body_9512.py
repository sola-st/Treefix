# Extracted from ./data/repos/tensorflow/tensorflow/python/client/session_partial_run_test.py
a = array_ops.placeholder(dtypes.float32, shape=[])
b = array_ops.placeholder(dtypes.float32, shape=[])
c = array_ops.placeholder(dtypes.float32, shape=[])
r1 = math_ops.add(a, b)

h = sess.partial_run_setup([r1], [a, b])
with self.assertRaisesRegex(errors.InvalidArgumentError,
                            'was not specified in partial_run_setup.$'):
    sess.partial_run(h, r1, feed_dict={a: 1, b: 2, c: 3})
