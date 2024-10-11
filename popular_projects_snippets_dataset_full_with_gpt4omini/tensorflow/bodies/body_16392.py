# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/nn_ops.py
"""Computes sums of N-D convolutions (actually cross correlation).

  It is required that 1 <= N <= 3.

  This is used to implement the more generic `convolution` function, which
  extends the interface of this function with a `dilation_rate` parameter.

  Args:

    input: Rank N+2 tensor of type T of shape
      `[batch_size] + input_spatial_shape + [in_channels]` if `data_format`
      does not start with `"NC"`, or
      `[batch_size, in_channels] + input_spatial_shape` if `data_format` starts
      with `"NC"`.
    filter: Rank N+2 tensor of type T of shape
      `filter_spatial_shape + [in_channels, out_channels]`.  Rank of either
      `input` or `filter` must be known.
    padding: Padding method to use, must be either "VALID" or "SAME".
    data_format: A string or None.  Specifies whether the channel dimension of
      the `input` and output is the last dimension (default, or if `data_format`
      does not start with "NC"), or the second dimension (if `data_format`
      starts with "NC").  For N=1, the valid values are "NWC" (default) and
      "NCW".  For N=2, the valid values are "NHWC" (default) and "NCHW".
      For N=3, the valid values are "NDHWC" (default) and "NCDHW".
    strides: Sequence of N positive integers, defaults to `[1] * N`.
    name: Name prefix to use.

  Returns:
    Rank N+2 tensor of type T of shape
    `[batch_size] + output_spatial_shape + [out_channels]`, where
    if padding == "SAME":
      output_spatial_shape = input_spatial_shape
    if padding == "VALID":
      output_spatial_shape = input_spatial_shape - filter_spatial_shape + 1.

  Raises:
    ValueError: if ranks are incompatible.

  """
with ops.name_scope(name, "non_atrous_convolution", [input, filter]) as scope:
    input = ops.convert_to_tensor(input, name="input")  # pylint: disable=redefined-builtin
    input_shape = input.shape
    filter = ops.convert_to_tensor(filter, name="filter")  # pylint: disable=redefined-builtin
    filter_shape = filter.shape
    op = _NonAtrousConvolution(
        input_shape,
        filter_shape=filter_shape,
        padding=padding,
        data_format=data_format,
        strides=strides,
        name=scope)
    exit(op(input, filter))
