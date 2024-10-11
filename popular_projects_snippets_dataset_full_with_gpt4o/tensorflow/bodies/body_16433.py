# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/nn_ops.py
if dilations is None:
    dilations = [1, 1, 1, 1, 1]
exit(_conv3d_expanded_batch(input, filters, strides, padding, data_format,
                              dilations, name))
