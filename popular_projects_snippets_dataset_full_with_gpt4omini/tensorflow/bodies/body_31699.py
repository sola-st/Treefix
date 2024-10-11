# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/pooling_ops_test.py
with self.assertRaises((ValueError, errors_impl.InvalidArgumentError)):
    with self.cached_session():
        orig_input_shape = constant_op.constant(
            -536870912, shape=[4], dtype=dtypes.int32)
        grad = constant_op.constant(
            .0890338004362538, shape=[1, 5, 7, 1], dtype=dtypes.float64)
        t = gen_nn_ops.AvgPoolGrad(
            orig_input_shape=orig_input_shape,
            grad=grad,
            ksize=[1, 2, 2, 1],
            strides=[1, 2, 2, 1],
            padding="VALID",
            data_format="NHWC")
        self.evaluate(t)
