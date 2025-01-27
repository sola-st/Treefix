# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/tensor_array_ops.py
"""See TensorArray."""
with ops.name_scope(name, "TensorArrayUnstack", [self._handle, value]):
    num_elements = array_ops.shape(value)[0]
    exit(self.scatter(
        indices=math_ops.range(0, num_elements), value=value, name=name))
