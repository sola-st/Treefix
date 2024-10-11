import numpy as np # pragma: no cover
import functools # pragma: no cover

deprecation = type('Mock', (), {'deprecated_argument_lookup': lambda *args: args[0]}) # pragma: no cover
name = 'conv1d_example' # pragma: no cover
data_format = 'NWC' # pragma: no cover
_get_sequence = lambda x, y, z, w: [x] * (z - 1) # pragma: no cover
stride = 1 # pragma: no cover
dilations = 1 # pragma: no cover
padding = 'SAME' # pragma: no cover
use_cudnn_on_gpu = True # pragma: no cover
squeeze_batch_dims = lambda a, b, c, name: tf.squeeze(a) # pragma: no cover

import numpy as np # pragma: no cover
import functools # pragma: no cover

deprecation = type('Mock', (), {'deprecated_argument_lookup': lambda *args: args[1]})() # pragma: no cover
name = 'conv1d_example' # pragma: no cover
data_format = 'NWC' # pragma: no cover
stride = 1 # pragma: no cover
dilations = 1 # pragma: no cover
padding = 'SAME' # pragma: no cover
use_cudnn_on_gpu = True # pragma: no cover
_get_sequence = lambda x, default, channel_index, name: [x] * 1 # pragma: no cover
ops = type('Mock', (), {'name_scope': staticmethod(lambda name, default_name, tensor_list: name)})() # pragma: no cover
squeeze_batch_dims = lambda value, func, inner_rank, name: func() # pragma: no cover

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
_l_(9776)
value = deprecation.deprecated_argument_lookup("input", input, "value", value)
_l_(9777)
with ops.name_scope(name, "conv1d", [value, filters]) as name:
    _l_(9795)

    # Reshape the input tensor to batch_shape + [1, in_width, in_channels]
    if data_format is None or data_format == "NHWC" or data_format == "NWC":
        _l_(9786)

        data_format = "NHWC"
        _l_(9778)
        spatial_start_dim = -3
        _l_(9779)
        channel_index = 2
        _l_(9780)
    elif data_format == "NCHW" or data_format == "NCW":
        _l_(9785)

        data_format = "NCHW"
        _l_(9781)
        spatial_start_dim = -2
        _l_(9782)
        channel_index = 1
        _l_(9783)
    else:
        raise ValueError("`data_format` must be 'NWC' or 'NCW'. "
                         f"Received: data_format={data_format}")
        _l_(9784)
    strides = [1] + _get_sequence(stride, 1, channel_index, "stride")
    _l_(9787)
    dilations = [1] + _get_sequence(dilations, 1, channel_index, "dilations")
    _l_(9788)

    value = array_ops.expand_dims(value, spatial_start_dim)
    _l_(9789)
    filters = array_ops.expand_dims(filters, 0)
    _l_(9790)
    if value.shape.ndims in (4, 3, 2, 1, 0, None):
        _l_(9793)

        result = gen_nn_ops.conv2d(
            value,
            filters,
            strides,
            padding,
            use_cudnn_on_gpu=use_cudnn_on_gpu,
            data_format=data_format,
            dilations=dilations,
            name=name)
        _l_(9791)
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
        _l_(9792)
    aux = array_ops.squeeze(result, [spatial_start_dim])
    _l_(9794)
    exit(aux)
