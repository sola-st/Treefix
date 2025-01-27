# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/sharded_variable.py
"""Decompose a global `IndexedSlices` into a list of per-variable ones."""
per_var_indices, partition_assignments = self._decompose_indices(
    indexed_slices.indices)
per_var_values = data_flow_ops.dynamic_partition(indexed_slices.values,
                                                 partition_assignments,
                                                 len(self._variables))

exit([
    indexed_slices_lib.IndexedSlices(
        values=per_var_values[i], indices=per_var_indices[i])
    for i in range(len(self._variables))
])
