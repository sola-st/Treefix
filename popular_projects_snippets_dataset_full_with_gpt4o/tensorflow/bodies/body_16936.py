# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/nn_impl.py
"""2-D convolution with separable filters.

  Performs a depthwise convolution that acts separately on channels followed by
  a pointwise convolution that mixes channels.  Note that this is separability
  between dimensions `[1, 2]` and `3`, not spatial separability between
  dimensions `1` and `2`.

  In detail, with the default NHWC format,

      output[b, i, j, k] = sum_{di, dj, q, r}
          input[b, strides[1] * i + di, strides[2] * j + dj, q] *
          depthwise_filter[di, dj, q, r] *
          pointwise_filter[0, 0, q * channel_multiplier + r, k]

  `strides` controls the strides for the depthwise convolution only, since
  the pointwise convolution has implicit strides of `[1, 1, 1, 1]`.  Must have
  `strides[0] = strides[3] = 1`.  For the most common case of the same
  horizontal and vertical strides, `strides = [1, stride, stride, 1]`.
  If any value in `rate` is greater than 1, we perform atrous depthwise
  convolution, in which case all values in the `strides` tensor must be equal
  to 1.

  Args:
    input: 4-D `Tensor` with shape according to `data_format`.
    depthwise_filter: 4-D `Tensor` with shape
      `[filter_height, filter_width, in_channels, channel_multiplier]`.
      Contains `in_channels` convolutional filters of depth 1.
    pointwise_filter: 4-D `Tensor` with shape
      `[1, 1, channel_multiplier * in_channels, out_channels]`.  Pointwise
      filter to mix channels after `depthwise_filter` has convolved spatially.
    strides: 1-D of size 4.  The strides for the depthwise convolution for
      each dimension of `input`.
    padding: Controls how to pad the image before applying the depthwise
      convolution. Can be the string `"SAME"` or `"VALID"` indicating the type
      of padding algorithm to use, or a Python list indicating the explicit
      paddings at the start and end of each dimension. When explicit padding is
      used and data_format is `"NHWC"`, this should be in the form `[[0, 0],
      [pad_top, pad_bottom], [pad_left, pad_right], [0, 0]]`. When explicit
      padding used and data_format is `"NCHW"`, this should be in the form
      `[[0, 0], [0, 0], [pad_top, pad_bottom], [pad_left, pad_right]]`.
    rate: 1-D of size 2. The dilation rate in which we sample input values
      across the `height` and `width` dimensions in atrous convolution. If it is
      greater than 1, then all values of strides must be 1.
    name: A name for this operation (optional).
    data_format: The data format for input. Either "NHWC" (default) or "NCHW".
    dilations: Alias of rate.

  Returns:
    A 4-D `Tensor` with shape according to 'data_format'. For
      example, with data_format="NHWC", shape is [batch, out_height,
      out_width, out_channels].
  """
rate = deprecated_argument_lookup("dilations", dilations, "rate", rate)
with ops.name_scope(name, "separable_conv2d",
                    [input, depthwise_filter, pointwise_filter]) as name:
    input = ops.convert_to_tensor(input, name="tensor_in")
    depthwise_filter = ops.convert_to_tensor(
        depthwise_filter, name="depthwise_filter")
    pointwise_filter = ops.convert_to_tensor(
        pointwise_filter, name="pointwise_filter")

    pointwise_filter_shape = pointwise_filter.get_shape().with_rank(4)
    pointwise_filter_shape.dims[0].assert_is_compatible_with(1)
    pointwise_filter_shape.dims[1].assert_is_compatible_with(1)

    if rate is None:
        rate = [1, 1]

    # The layout of the ops in the graph are expected to be as follows:
    # depthwise_conv2d  // Conv2D op corresponding to native depthwise conv.
    # separable_conv2d  // Conv2D op corresponding to the pointwise conv.

    def op(input_converted, _, padding):
        exit(nn_ops.depthwise_conv2d_native(
            input=input_converted,
            filter=depthwise_filter,
            strides=strides,
            padding=padding,
            data_format=data_format,
            name="depthwise"))

    depthwise = nn_ops.with_space_to_batch(
        input=input,
        filter_shape=array_ops.shape(depthwise_filter),
        dilation_rate=rate,
        padding=padding,
        data_format=data_format,
        op=op)

    exit(nn_ops.conv2d(
        depthwise,
        pointwise_filter, [1, 1, 1, 1],
        padding="VALID",
        data_format=data_format,
        name=name))
