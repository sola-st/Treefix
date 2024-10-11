# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/nn_ops.py
"""Performs the max pooling on the input.

  Args:
    value: A 4-D `Tensor` of the format specified by `data_format`.
    ksize: An int or list of `ints` that has length `1`, `2` or `4`.
      The size of the window for each dimension of the input tensor.
    strides: An int or list of `ints` that has length `1`, `2` or `4`.
      The stride of the sliding window for each dimension of the input tensor.
    padding: Either the `string` `"SAME"` or `"VALID"` indicating the type of
      padding algorithm to use, or a list indicating the explicit paddings at
      the start and end of each dimension. When explicit padding is used and
      data_format is `"NHWC"`, this should be in the form `[[0, 0], [pad_top,
      pad_bottom], [pad_left, pad_right], [0, 0]]`. When explicit padding used
      and data_format is `"NCHW"`, this should be in the form `[[0, 0], [0, 0],
      [pad_top, pad_bottom], [pad_left, pad_right]]`. When using explicit
      padding, the size of the paddings cannot be greater than the sliding
      window size.
    data_format: A string. 'NHWC', 'NCHW' and 'NCHW_VECT_C' are supported.
    name: Optional name for the operation.
    input: Alias for value.

  Returns:
    A `Tensor` of format specified by `data_format`.
    The max pooled output tensor.
  """
value = deprecation.deprecated_argument_lookup("input", input, "value", value)
with ops.name_scope(name, "MaxPool", [value]) as name:
    if data_format is None:
        data_format = "NHWC"
    channel_index = 1 if data_format.startswith("NC") else 3

    ksize = _get_sequence(ksize, 2, channel_index, "ksize")
    strides = _get_sequence(strides, 2, channel_index, "strides")
    if isinstance(padding, (list, tuple)) and data_format == "NCHW_VECT_C":
        raise ValueError("`data_format='NCHW_VECT_C'` is not supported with "
                         f"explicit padding. Received: padding={padding}")
    padding, explicit_paddings = convert_padding(padding)
    if ((np.isscalar(ksize) and ksize == 0) or
        (isinstance(ksize,
                    (list, tuple, np.ndarray)) and any(v == 0 for v in ksize))):
        raise ValueError(f"`ksize` cannot be zero. Received: ksize={ksize}")

    exit(gen_nn_ops.max_pool(
        value,
        ksize=ksize,
        strides=strides,
        padding=padding,
        explicit_paddings=explicit_paddings,
        data_format=data_format,
        name=name))
