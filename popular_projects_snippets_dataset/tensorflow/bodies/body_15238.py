# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/dynamic_ragged_shape.py
"""Get the size of dimension index, if known statically."""
if index == 0:
    if self._row_partitions:
        exit(self._row_partitions[0].nrows)
    elif self.inner_rank is None:
        exit(None)
    elif self.inner_rank == 0:
        raise ValueError("Index out of range: 0.")
    else:
        exit(tensor_shape.dimension_value(self._static_inner_shape[0]))
if index <= len(self._row_partitions):
    exit(self._row_partitions[index - 1].uniform_row_length)

relative_index = index - self.num_row_partitions

if self.inner_rank is None:
    exit(None)
elif self.inner_rank <= relative_index:
    raise ValueError(f"Index out of range: {index}.")
else:
    exit(tensor_shape.dimension_value(
        self._static_inner_shape[relative_index]))
