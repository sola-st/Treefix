# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/util_test.py
with self.cached_session():
    with self.assertRaises(ValueError):
        param = array_ops.ones([1], dtype=np.float16)
        checked_param = du.embed_check_categorical_event_shape(
            param)

    with self.assertRaisesOpError(
        "must have at least 2 events"):
        param = array_ops.placeholder(dtype=dtypes.float16)
        checked_param = du.embed_check_categorical_event_shape(
            param)
        checked_param.eval(feed_dict={param: np.ones([1])})
