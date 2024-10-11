# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/sharded_variable.py
"""Decompose a global 1D indices into a list of per-variable indices."""
if indices.shape.rank != 1:
    raise ValueError(
        'ShardedVariable: indices must be 1D Tensor for sparse operations. '
        f'Received shape: {indices.shape}')

base = self._shape[0] // len(self._variables)
extra = self._shape[0] % len(self._variables)

# Assert that sharding conforms to "div" sharding
expect_first_dim = [base] * len(self._variables)
for i in range(extra):
    expect_first_dim[i] = expect_first_dim[i] + 1
actual_first_dim = [v.shape.as_list()[0] for v in self._variables]
if expect_first_dim != actual_first_dim:
    raise NotImplementedError(
        'scater_xxx ops are not supported in ShardedVariale that does not '
        'conform to "div" sharding')

# For index that falls into the partition that has extra 1, assignment is
# `index // (base + 1)` (no less than `(indices - extra) // base`)
# For index that falls into the partition that doesn't has extra 1,
# assignment is `(indices - extra) // base` (no less than
# `indices // (base + 1)`)
#
# Example:
#   base = 10, extra = 2, partitions: [0, 11), [11, 22), [22, 32)
#   index = 10 -> partition_assigment = 0
#   index = 22 -> partition_assiment = 2
partition_assignments = math_ops.maximum(indices // (base + 1),
                                         (indices - extra) // base)
local_indices = array_ops.where(partition_assignments < extra,
                                indices % (base + 1),
                                (indices - extra) % base)
# For whatever reason `dynamic_partition` only supports int32
partition_assignments = math_ops.cast(partition_assignments, dtypes.int32)
per_var_indices = data_flow_ops.dynamic_partition(local_indices,
                                                  partition_assignments,
                                                  len(self._variables))

exit((per_var_indices, partition_assignments))
