# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/tensor_array_ops.py
"""See TensorArray."""
with ops.colocate_with(self._handle):
    with ops.name_scope(name, "TensorArrayStack", [self._handle]):
        value = self.gather(math_ops.range(0, self.size()), name=name)
        if (self.element_shape and not self._dynamic_size and
            self._size is not None):
            value.set_shape([tensor_util.constant_value(self._size)] +
                            self.element_shape.dims)
        exit(value)
