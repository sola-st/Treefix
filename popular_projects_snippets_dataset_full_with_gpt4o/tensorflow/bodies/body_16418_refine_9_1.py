import functools # pragma: no cover

deprecation = type('Mock', (object,), {'deprecated_argument_lookup': lambda a, b, c, d: d if d is not None else b})() # pragma: no cover

import functools # pragma: no cover

input = None # pragma: no cover
data_format = 'NWC' # pragma: no cover
def _get_sequence(value, n, channel_index, name):# pragma: no cover
    if isinstance(value, int):# pragma: no cover
        return [value] * n# pragma: no cover
    return value # pragma: no cover
stride = 1 # pragma: no cover
dilations = 1 # pragma: no cover
padding = 'SAME' # pragma: no cover
use_cudnn_on_gpu = True # pragma: no cover
squeeze_batch_dims = lambda value, conv_op, inner_rank, name: conv_op(value) # pragma: no cover
functools = functools # pragma: no cover
deprecation = type('Mock', (object,), {'deprecated_argument_lookup': lambda alias, input, name, value: value if value is not None else input})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/nn_ops.py
from l3.Runtime import _l_
r"""Computes a 1-D convolution of input with rank `>=3` and a `3-D` filter.

  Given an input tensor of shape
    `batch_shape + [in_width, in_channels]`
  if `data_format` is `"NWC"`, or
    `batch_shape + [in_channels, in_width]`
  if `data_format` is `"NCW"`,
  and a filter / kernel tensor of shape
  `[filter_width, in_channels, out_channels]`, this op reshapes
  the arguments to pass them to `conv2d` to perform the equivalent
  convolution operation.

  Internally, this op reshapes the input tensors and invokes `tf.nn.conv2d`.
  For example, if `data_format` does not start with "NC", a tensor of shape
    `batch_shape + [in_width, in_channels]`
  is reshaped to
    `batch_shape + [1, in_width, in_channels]`,
  and the filter is reshaped to
    `[1, filter_width, in_channels, out_channels]`.
  The result is then reshaped back to
    `batch_shape + [out_width, out_channels]`
  \(where out_width is a function of the stride and padding as in conv2d\) and
  returned to the caller.

  Args:
    value: A Tensor of rank at least 3. Must be of type `float16`, `float32`, or
      `float64`.
    filters: A Tensor of rank at least 3.  Must have the same type as `value`.
    stride: An int or list of `ints` that has length `1` or `3`.  The number of
      entries by which the filter is moved right at each step.
    padding: 'SAME' or 'VALID'
    use_cudnn_on_gpu: An optional `bool`.  Defaults to `True`.
    data_format: An optional `string` from `"NWC", "NCW"`.  Defaults to `"NWC"`,
      the data is stored in the order of `batch_shape + [in_width,
      in_channels]`.  The `"NCW"` format stores data as `batch_shape +
      [in_channels, in_width]`.
    name: A name for the operation (optional).
    input: Alias for value.
    dilations: An int or list of `ints` that has length `1` or `3` which
      defaults to 1. The dilation factor for each dimension of input. If set to
      k > 1, there will be k-1 skipped cells between each filter element on that
      dimension. Dilations in the batch and depth dimensions must be 1.

  Returns:
    A `Tensor`.  Has the same type as input.

  Raises:
    ValueError: if `data_format` is invalid.
  """
_l_(22068)
value = deprecation.deprecated_argument_lookup("input", input, "value", value)
_l_(22069)
with ops.name_scope(name, "conv1d", [value, filters]) as name:
    _l_(22087)

    # Reshape the input tensor to batch_shape + [1, in_width, in_channels]
    if data_format is None or data_format == "NHWC" or data_format == "NWC":
        _l_(22078)

        data_format = "NHWC"
        _l_(22070)
        spatial_start_dim = -3
        _l_(22071)
        channel_index = 2
        _l_(22072)
    elif data_format == "NCHW" or data_format == "NCW":
        _l_(22077)

        data_format = "NCHW"
        _l_(22073)
        spatial_start_dim = -2
        _l_(22074)
        channel_index = 1
        _l_(22075)
    else:
        raise ValueError("`data_format` must be 'NWC' or 'NCW'. "
                         f"Received: data_format={data_format}")
        _l_(22076)
    strides = [1] + _get_sequence(stride, 1, channel_index, "stride")
    _l_(22079)
    dilations = [1] + _get_sequence(dilations, 1, channel_index, "dilations")
    _l_(22080)

    value = array_ops.expand_dims(value, spatial_start_dim)
    _l_(22081)
    filters = array_ops.expand_dims(filters, 0)
    _l_(22082)
    if value.shape.ndims in (4, 3, 2, 1, 0, None):
        _l_(22085)

        result = gen_nn_ops.conv2d(
            value,
            filters,
            strides,
            padding,
            use_cudnn_on_gpu=use_cudnn_on_gpu,
            data_format=data_format,
            dilations=dilations,
            name=name)
        _l_(22083)
    else:
        result = squeeze_batch_dims(
            value,
            functools.partial(
                gen_nn_ops.conv2d,
                filter=filters,
                strides=strides,
                padding=padding,
                use_cudnn_on_gpu=use_cudnn_on_gpu,
                data_format=data_format,
                dilations=dilations,
            ),
            inner_rank=3,
            name=name)
        _l_(22084)
    aux = array_ops.squeeze(result, [spatial_start_dim])
    _l_(22086)
    exit(aux)
