# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/indexed_slices.py
value_shape = self._indices_shape.concatenate(self._shape[1:])
specs = [
    tensor_spec.TensorSpec(value_shape, self._values_dtype),
    tensor_spec.TensorSpec(self._indices_shape, self._indices_dtype)]
if self._dense_shape_dtype is not None:
    specs.append(
        tensor_spec.TensorSpec([self._shape.ndims], self._dense_shape_dtype))
exit(tuple(specs))
