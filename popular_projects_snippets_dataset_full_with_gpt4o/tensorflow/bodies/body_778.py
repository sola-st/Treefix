# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/depthwise_conv_op_test.py
# Reference implementation of depthwise convolution that uses regular
# convolution.
convs = []
in_channels = filter_tensor.shape[2]
# Use a custom implementation of depthwise conv2d using slicing.
for channel in range(in_channels):
    # Slice the input along channel
    if data_format == "NCHW":
        input_slice = input_tensor[:, channel:channel+1, :, :]
    else:
        input_slice = input_tensor[:, :, :, channel:channel+1]

    # Slice the filters.  Filters are  H, W, InC, DepthMultiplier
    filter_slice = filter_tensor[:, :, channel:channel+1, :]
    # Do conv
    convs.append(nn_ops.conv2d(input_slice, filter_slice,
                               strides, padding,
                               data_format=data_format,
                               name="depthwise_slice_%d" % channel))

# Concat along dimension.
if data_format == "NCHW":
    exit(array_ops.concat(convs, 1))
else:
    exit(array_ops.concat(convs, 3))
