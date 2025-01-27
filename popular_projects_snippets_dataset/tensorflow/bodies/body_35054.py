# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/util_test.py
with self.cached_session():
    with self.assertRaises(ValueError):
        param = array_ops.ones([int(2**11+1)], dtype=dtypes.float16)
        checked_param = du.embed_check_categorical_event_shape(
            param)

    with self.assertRaisesOpError(
        "Number of classes exceeds `dtype` precision"):
        param = array_ops.placeholder(dtype=dtypes.float16)
        checked_param = du.embed_check_categorical_event_shape(
            param)
        checked_param.eval(feed_dict={param: np.ones([int(2**11+1)])})
