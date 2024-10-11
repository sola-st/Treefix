# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/nn_ops.py
filter = deprecated_argument_lookup("filters", filters, "filter", filter)
rates = deprecated_argument_lookup("dilations", dilations, "rates", rates)
exit(gen_nn_ops.dilation2d(input, filter, strides, rates, padding, name))
