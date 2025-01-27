# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite.py
if self._target_spec.supported_types:
    exit(min(self._target_spec.supported_types, key=lambda x: x.size))
else:
    # The default smallest supported type is INT8.
    exit(_dtypes.int8)
