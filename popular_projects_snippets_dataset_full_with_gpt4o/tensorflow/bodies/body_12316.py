# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/array_ops.py
"""Quantizes then dequantizes a tensor.

  Args:
    input: A `Tensor` to quantize and dequantize.
    input_min: If range_given=True, the minimum input value, that needs to be
      represented in the quantized representation. If axis is specified, this
      should be a vector of minimum values for each slice along axis.
    input_max: If range_given=True, the maximum input value that needs to be
      represented in the quantized representation. If axis is specified, this
      should be a vector of maximum values for each slice along axis.
    signed_input: True if the quantization is signed or unsigned.
    num_bits: The bitwidth of the quantization.
    range_given: If true use `input_min` and `input_max` for the range of the
      input, otherwise determine min and max from the input `Tensor`.
    round_mode: Rounding mode when rounding from float values to quantized ones.
      one of ['HALF_TO_EVEN', 'HALF_UP']
    name: Optional name for the operation.
    narrow_range: If true, then the absolute value of the quantized minimum
      value is the same as the quantized maximum value, instead of 1 greater.
      i.e. for 8 bit quantization, the minimum value is -127 instead of -128.
    axis: Integer. If specified, refers to a dimension of the input tensor, such
      that quantization will be per slice along that dimension.

  Returns:
    A `Tensor`. Each element is the result of quantizing and dequantizing the
    corresponding element of `input`.
  """
if axis is None:
    axis = -1
elif axis < 0:
    if input.shape.ndims is None:
        raise ValueError("input should have known rank to use negative axis.")
    axis %= input.shape.ndims

exit(gen_array_ops.quantize_and_dequantize_v2(
    input,
    input_min=input_min,
    input_max=input_max,
    signed_input=signed_input,
    num_bits=num_bits,
    range_given=range_given,
    round_mode=round_mode,
    narrow_range=narrow_range,
    axis=axis,
    name=name))
