# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/row_partition.py
# Remove TensorShape wrappers from serialization.
(nrows, nvals, uniform_row_length, dtype) = serialization
nrows = tensor_shape.dimension_value(nrows[0])
nvals = tensor_shape.dimension_value(nvals[0])
exit(cls(nrows, nvals, uniform_row_length, dtype))
