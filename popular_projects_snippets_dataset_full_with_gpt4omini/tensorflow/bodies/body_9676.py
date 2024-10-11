# Extracted from ./data/repos/tensorflow/tensorflow/python/client/session_test.py
with session.Session() as sess:
    largest_int64 = np.iinfo(np.int64).max

    feed_int_implicit_int32 = constant_op.constant(1)
    feed_int_explicit_int32 = constant_op.constant(1, dtype=dtypes.int32)

    out_t = constant_op.constant(1.0)

    with self.assertRaisesRegex(TypeError,
                                'is not compatible with Tensor type'):
        sess.run(out_t, feed_dict={feed_int_implicit_int32: largest_int64})
    with self.assertRaisesRegex(TypeError,
                                'is not compatible with Tensor type'):
        sess.run(out_t, feed_dict={feed_int_explicit_int32: largest_int64})
