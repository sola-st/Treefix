# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/nn_ops.py
filter = deprecated_argument_lookup("filters", filters, "filter", filter)
exit(gen_nn_ops.conv3d(
    input, filter, strides, padding, data_format, dilations, name))
