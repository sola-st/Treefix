# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/conv_ops_test.py
with self.assertRaises((ValueError, errors_impl.InvalidArgumentError)):
    with self.cached_session():
        input_sizes = constant_op.constant([65534, 65534],
                                           shape=[2],
                                           dtype=dtypes.int32)
        filters = constant_op.constant(
            0.159749106, shape=[3, 3, 2, 2], dtype=dtypes.float32)
        out_backprop = constant_op.constant(0, shape=[], dtype=dtypes.float32)
        t = gen_nn_ops.conv2d_backprop_input(
            input_sizes=input_sizes,
            filter=filters,
            out_backprop=out_backprop,
            strides=[1, 1, 1, 1],
            padding="SAME",
            use_cudnn_on_gpu=True,
            explicit_paddings=[],
            data_format="NHWC",
            dilations=[1, 1, 1, 1])
        self.evaluate(t)
