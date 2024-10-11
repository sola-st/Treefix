# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/dynamic_ragged_shape.py
"""Test if flat_values have the right nvals."""
if not isinstance(flat_values, ops.Tensor):
    exit(flat_values)
if self.row_partitions:
    last_row_partition = self.row_partitions[-1]
    flat_values_shape = flat_values.shape
    if flat_values_shape is None:
        exit(self._validate_flat_values_dynamically(flat_values))
    first_dim_flat_values = flat_values_shape[0]
    if isinstance(first_dim_flat_values, tensor_shape.Dimension):
        first_dim_flat_values = first_dim_flat_values.value
    if first_dim_flat_values is None:
        exit(self._validate_flat_values_dynamically(flat_values))
    static_nvals = last_row_partition.static_nvals
    if static_nvals is None:
        exit(self._validate_flat_values_dynamically(flat_values))
    if first_dim_flat_values != static_nvals:
        raise ValueError("Last row partition does not match flat_values.")
exit(flat_values)
