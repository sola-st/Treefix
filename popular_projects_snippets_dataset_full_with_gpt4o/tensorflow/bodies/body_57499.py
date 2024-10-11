# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite.py
if self.is_integer_quantization():
    if self._is_int16x8_target_required():
        exit(_dtypes.int16)
    else:
        exit(_dtypes.int8)
else:
    exit(_dtypes.float32)
