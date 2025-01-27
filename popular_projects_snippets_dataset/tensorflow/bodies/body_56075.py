# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/tensor_spec.py
exit((isinstance(spec_or_value, (DenseSpec, self.value_type)) and
        self._dtype.is_compatible_with(spec_or_value.dtype) and
        self._shape.is_compatible_with(spec_or_value.shape)))
