# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/conv_ops_test.py
with self.assertRaisesRegex((ValueError, errors_impl.InvalidArgumentError),
                            "Encountered overflow"):
    mode = "REFLECT"
    strides = [1, 1, 1, 1]
    padding = "SAME"
    resize_align_corners = False
    tensor = constant_op.constant(
        147, shape=[3, 3, 1, 4], dtype=dtypes.float32)
    size = constant_op.constant([1879048192, 1879048192], dtype=dtypes.int32)
    paddings = constant_op.constant([[0, 0], [0, 0], [0, 0], [0, 0]],
                                    dtype=dtypes.int32)
    kernel = constant_op.constant(
        123, shape=[1, 3, 4, 1], dtype=dtypes.float32)
    self.evaluate(
        gen_nn_ops.fused_resize_and_pad_conv2d(
            input=tensor,
            size=size,
            paddings=paddings,
            filter=kernel,
            mode=mode,
            strides=strides,
            padding=padding,
            resize_align_corners=resize_align_corners))
