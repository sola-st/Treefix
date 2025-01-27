# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/ops/tpu_ops.py
"""Exchange data across TPU replicas.

  Args:
    x: The local tensor.
    concat_dimension: The dimension number to concatenate.
    split_dimension: The dimension number to split.
    split_count: The number of splits, this number must equal to the sub-group
      size(group_assignment.get_shape()[1])
    group_assignment: Optional 2d int32 lists with shape [num_groups,
      num_replicas_per_group]. `group_assignment[i]` represents the replica ids
      in the ith subgroup.
    name: Optional op name.

  Returns:
    A `Tensor` which is concatenated by data from different replicas.
  """
if group_assignment is None:
    group_assignment = _create_default_group_assignment()
exit(gen_tpu_ops.all_to_all(
    x,
    group_assignment,
    concat_dimension=concat_dimension,
    split_dimension=split_dimension,
    split_count=split_count,
    name=name))
