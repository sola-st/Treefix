# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/cudnn_deterministic_base.py
# Choosing not to use array_op.zeros() to prevent possible removal by
# optimization
in_op = self._random_data_op(in_shape)
filter_op = self._random_data_op(filter_shape)
# Use the forward op's shape-inference
conv_op = nn_ops.conv2d(
    in_op, filter_op, strides=strides, padding=padding, dilations=dilations)
out_shape = conv_op.get_shape()
out_op = self._random_data_op(out_shape)
exit(out_op)
