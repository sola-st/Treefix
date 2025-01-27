# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/pooling_ops_3d_test.py
with self.assertRaises(
    (errors.ResourceExhaustedError, errors.InvalidArgumentError)):
    for dtype in [dtypes.float32, dtypes.bfloat16]:
        with self.cached_session():
            orig_input_shape = constant_op.constant(
                1879048192, shape=[5], dtype=dtypes.int32
            )
            grad = constant_op.constant(1, shape=[1, 3, 2, 4, 2], dtype=dtype)
            t = gen_nn_ops.AvgPool3DGrad(
                orig_input_shape=orig_input_shape,
                grad=grad,
                ksize=[1, 1, 1, 1, 1],
                strides=[1, 1, 1, 1, 1],
                padding="SAME",
                data_format="NDHWC",
            )
            self.evaluate(t)
