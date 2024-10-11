# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/ops/tpu_ops.py
"""Sum the input tensor across replicas according to group_assignment.

  Args:
    x: The local tensor to the sum.
    group_assignment: Optional 2d int32 lists with shape [num_groups,
      num_replicas_per_group]. `group_assignment[i]` represents the replica ids
      in the ith subgroup.
    name: Optional op name.

  Returns:
    A `Tensor` which is summed across replicas.
  """
if group_assignment is None:
    group_assignment = _create_default_group_assignment()

exit(gen_tpu_ops.cross_replica_sum(x, group_assignment, name=name))
