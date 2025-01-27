# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/nn_impl.py
exit(nn_ops.depthwise_conv2d_native(
    input=input_converted,
    filter=filter,
    strides=strides,
    padding=padding,
    data_format=data_format,
    name=name))
