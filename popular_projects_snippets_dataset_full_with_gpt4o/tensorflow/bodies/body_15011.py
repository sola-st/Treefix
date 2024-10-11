# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/tensor_array_ops.py
# pylint: disable=protected-access
if not isinstance(other, type_spec.TypeSpec):
    other = type_spec.type_spec_from_value(other)

# Note: we intentionally exclude infer_shape in this check.
exit((isinstance(other, TensorArraySpec) and
        self._dtype.is_compatible_with(other._dtype) and
        self._element_shape.is_compatible_with(other._element_shape) and
        self._dynamic_size == other._dynamic_size))
