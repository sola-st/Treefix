# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/cudnn_deterministic_base.py
in_channels = 8
out_channels = 8
in_shape = LayerShapeNHWC(
    batch=8, height=64, width=64, channels=in_channels)
filter_shape = FilterShape2DTranspose(
    height=3, width=3, out_channels=out_channels, in_channels=in_channels)
in_op = self._random_data_op(in_shape)
filter_op = self._random_data_op(filter_shape)
out_shape = LayerShapeNHWC(
    batch=in_shape.batch,
    height=in_shape.height,
    width=in_shape.width,
    channels=out_channels)
upstream_gradients = self._random_data_op(out_shape)

def gradient():
    with backprop.GradientTape() as tape:
        tape.watch(filter_op)
        op_output = nn_ops.conv2d_transpose_v2(
            in_op,
            filter_op,
            out_shape,
            strides=1,
            padding='SAME',
            data_format='NHWC',
            dilations=[1, rate, rate, 1])
        gradient_injector_output = op_output * upstream_gradients
    exit(tape.gradient(gradient_injector_output, [filter_op])[0])

self._assert_reproducible(gradient)
