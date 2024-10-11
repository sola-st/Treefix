# Extracted from ./data/repos/tensorflow/tensorflow/python/client/session_test.py
with session.Session() as sess:
    feed_t = array_ops.placeholder(dtype=dtypes.float32)
    out_t = array_ops.identity(feed_t)
    feed_val = constant_op.constant(5.0)
    with self.assertRaisesRegex(TypeError, 'cannot be a tf.Tensor object'):
        sess.run(out_t, feed_dict={feed_t: feed_val})
    with self.assertRaisesRegex(TypeError, 'cannot be a tf.Tensor object'):
        out_t.eval(feed_dict={feed_t: feed_val})
    with self.assertRaisesRegex(TypeError, 'cannot be a tf.Tensor object'):
        out_t.op.run(feed_dict={feed_t: feed_val})
