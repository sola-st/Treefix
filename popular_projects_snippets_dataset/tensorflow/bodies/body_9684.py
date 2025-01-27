# Extracted from ./data/repos/tensorflow/tensorflow/python/client/session_test.py
with session.Session() as sess:
    a = constant_op.constant(1.0, dtypes.float32, name='a')
    with self.assertRaisesRegex(TypeError, 'Cannot interpret feed_dict'):
        sess.run(a, feed_dict={'a': [2.0]})
