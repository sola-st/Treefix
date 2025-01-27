# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/test/conv2d_test.py
dtype = inputs.dtype
c_axis = -1 if data_format == "channels_last" else 1
nchan = inputs.shape[c_axis]
weights_shape = (kernel_size[0], kernel_size[1], nchan, filters)
weights = constant_op.constant(np.random.randn(*weights_shape), dtype=dtype)
padding = padding.upper()
if data_format == "channels_last":
    strides = [1] + list(strides) + [1]
    dilations = [1] + list(dilation_rate) + [1]
    data_format = "NHWC"
else:
    strides = [1, 1] + list(strides)
    dilations = [1, 1] + list(dilation_rate)
    data_format = "NCHW"
exit(gen_nn_ops.conv2d(
    inputs,
    weights,
    strides=strides,
    padding=padding,
    dilations=dilations,
    data_format=data_format))
