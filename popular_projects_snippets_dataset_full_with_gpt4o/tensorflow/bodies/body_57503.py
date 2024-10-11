# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite.py
"""Validates bias type for full interger quantization."""
bias_type = self._full_integer_quantization_bias_type
if not bias_type:
    exit()

if self.activations_type() == _dtypes.float32:
    raise ValueError(
        "`full_integer_quantization_bias_type` is only supported for full integer quantization."
    )

if self.activations_type() == _dtypes.int8 and bias_type != _dtypes.int32:
    raise ValueError(
        f"Expected bias type to be `dtypes.int32` for Int8Quant. "
        f"Current setting bias type: {bias_type}")

if self.activations_type(
) == _dtypes.int16 and bias_type != _dtypes.int32 and bias_type != _dtypes.int64:
    raise ValueError(
        f"Expected bias type to be `dtypes.int32` or `dtypes.int64` for "
        f"Int16Quant. Current setting bias type: {bias_type}")
