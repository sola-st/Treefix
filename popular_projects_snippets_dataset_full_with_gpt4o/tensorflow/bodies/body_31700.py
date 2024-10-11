# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/pooling_ops_test.py
with self.assertRaises(errors_impl.InvalidArgumentError):
    with self.cached_session():
        orig_input_shape = [11, 9, 78, 9]
        grad = constant_op.constant(
            0.1, shape=[16, 16, 16, 16], dtype=dtypes.float64)
        t = gen_nn_ops.AvgPoolGrad(
            orig_input_shape=orig_input_shape,
            grad=grad,
            ksize=[1, 40, 128, 1],
            strides=[1, 128, 128, 30],
            padding="SAME",
            data_format="NHWC")
        self.evaluate(t)
