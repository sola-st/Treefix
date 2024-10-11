# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/pooling_ops_test.py
with self.assertRaises((ValueError, errors_impl.InvalidArgumentError)):
    with self.cached_session():
        t = gen_nn_ops.avg_pool(
            value=np.ones([1, 1, 1, 1]),
            ksize=[1, 9223372036854775807, 1, 1],
            strides=[1, 1, 1, 1],
            padding="SAME",
            data_format="NHWC")
        self.evaluate(t)
