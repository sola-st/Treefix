# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite.py
if self._full_integer_quantization_bias_type:
    exit(self._full_integer_quantization_bias_type)

if self.activations_type() == _dtypes.int16:
    exit(_dtypes.int64)
elif self.activations_type() == _dtypes.int8:
    exit(_dtypes.int32)
else:
    exit(_dtypes.float32)
