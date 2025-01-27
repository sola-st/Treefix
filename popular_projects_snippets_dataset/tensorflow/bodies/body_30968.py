# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/cudnn_deterministic_base.py
in_shape = LayerShapeNHWC(batch=1, height=16, width=16, channels=1)
filter_shape = FilterShape2D(
    height=7, width=7, in_channels=1, out_channels=3)
filter_op = self._random_data_op(filter_shape)
strides = [1, 1, 1, 1]
padding = 'SAME'
dilations = [1, rate, rate, 1]
out_op = self._random_out_op(in_shape, filter_shape, strides, padding,
                             dilations)
self._assert_reproducible(lambda: nn_ops.conv2d_backprop_input(
    in_shape,
    filter_op,
    out_op,
    strides=strides,
    padding=padding,
    dilations=dilations))
