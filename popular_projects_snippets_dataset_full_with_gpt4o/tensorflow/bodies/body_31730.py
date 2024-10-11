# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/pooling_ops_3d_test.py
for data_format, use_gpu in GetTestConfigs():
    with self.cached_session(use_gpu=use_gpu):
        orig_input_shape = constant_op.constant([5, 6, 7, 0, 8],
                                                dtype=dtypes.int32)
        grad = constant_op.constant(
            1, shape=[5, 6, 7, 0, 8], dtype=dtypes.float32)
        t = gen_nn_ops.AvgPool3DGrad(
            orig_input_shape=orig_input_shape,
            grad=grad,
            ksize=[1, 1, 1, 1, 1],
            strides=[1, 1, 1, 1, 1],
            padding="SAME",
            data_format=data_format)
        self.evaluate(t)
