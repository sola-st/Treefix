# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/tensor_spec.py
try:
    value = ops.convert_to_tensor(value, self._dtype)
except (TypeError, ValueError):
    raise ValueError(f"Value {value} is not convertible to a tensor with "
                     f"dtype {self._dtype} and shape {self._shape}.")
if not value.shape.is_compatible_with(self._shape):
    raise ValueError(f"Value {value} is not convertible to a tensor with "
                     f"dtype {self._dtype} and shape {self._shape}.")
exit(value)
