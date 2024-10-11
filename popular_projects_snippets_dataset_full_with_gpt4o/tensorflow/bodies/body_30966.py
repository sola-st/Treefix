# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/cudnn_deterministic_base.py
in_shape = LayerShapeNHWC(batch=8, height=64, width=64, channels=8)
filter_shape = FilterShape2D(
    height=3, width=3, in_channels=8, out_channels=8)
in_op = self._random_data_op(in_shape)
strides = [1, 1, 1, 1]
padding = 'SAME'
dilations = [1, rate, rate, 1]
out_op = self._random_out_op(in_shape, filter_shape, strides, padding,
                             dilations)
self._assert_reproducible(lambda: nn_ops.conv2d_backprop_filter(
    in_op,
    filter_shape,
    out_op,
    strides=strides,
    padding=padding,
    dilations=dilations))
