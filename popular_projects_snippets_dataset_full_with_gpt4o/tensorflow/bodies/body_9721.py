# Extracted from ./data/repos/tensorflow/tensorflow/python/client/session_test.py
with self.cached_session() as sess:
    a = array_ops.placeholder(dtype=dtypes.string)
    with self.assertRaisesRegex(
        TypeError, r'Type of feed value 1 with type <(\w+) \'int\'> is not'):
        sess.run(a, feed_dict={a: 1})
