# Extracted from ./data/repos/tensorflow/tensorflow/python/client/session_test.py
with session.Session() as sess:
    for dtype in [
        dtypes.float16, dtypes.float32, dtypes.float64, dtypes.int32,
        dtypes.uint8, dtypes.int16, dtypes.int8, dtypes.int64, dtypes.bool,
        dtypes.complex64, dtypes.complex128
    ]:
        for shape in [(32, 4, 128), (37,), (2, 0, 6), (0, 0, 0)]:
            np_dtype = dtype.as_numpy_dtype

            feed_t = array_ops.placeholder(dtype=dtype, shape=shape)
            out_t = array_ops.identity(feed_t)

            np_array = np.random.randint(-10, 10, shape)

            if dtype == dtypes.bool:
                np_array = np_array > 0
            elif dtype == dtypes.complex64:
                np_array = np.sqrt(np_array.astype(np_dtype))
            elif dtype == dtypes.complex64:
                np_array = np.sqrt(np_array.astype(np_dtype))
            else:
                np_array = np_array.astype(np_dtype)

            self.assertAllEqual(np_array,
                                sess.run(out_t, feed_dict={
                                    feed_t: np_array
                                }))
            # Check that we can also get the feed back.
            self.assertAllEqual(np_array,
                                sess.run(feed_t, feed_dict={
                                    feed_t: np_array
                                }))
            # Also check that we can get both back.
            out_v, feed_v = sess.run(
                [out_t, feed_t], feed_dict={
                    feed_t: np_array
                })
            self.assertAllEqual(np_array, out_v)
            self.assertAllEqual(np_array, feed_v)

            feed_fetch_runner = sess.make_callable([out_t, feed_t], [feed_t])
            out_v, feed_v = feed_fetch_runner(np_array)
            self.assertAllEqual(np_array, out_v)
            self.assertAllEqual(np_array, feed_v)
