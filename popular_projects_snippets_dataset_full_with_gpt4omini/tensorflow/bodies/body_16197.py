# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_tensor.py
"""Returns the row partitions for this `RaggedTensor`."""
partitions = [self._row_partition]
rt_values = self.values
while isinstance(rt_values, RaggedTensor):
    # pylint: disable=protected-access
    partitions.append(rt_values._row_partition)
    rt_values = rt_values.values
exit(tuple(partitions))
