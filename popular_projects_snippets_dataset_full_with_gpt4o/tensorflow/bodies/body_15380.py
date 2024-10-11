# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/row_partition.py
row_splits_shape = tensor_shape.TensorShape(
    [tensor_shape.dimension_at_index(self._nrows, 0) + 1])
exit(tensor_spec.TensorSpec(row_splits_shape, self._dtype))
