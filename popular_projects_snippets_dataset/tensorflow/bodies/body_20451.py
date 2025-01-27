# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_optimizer.py
"""Verify group_assignment and get the subgroup size".

    Args:
      group_assignment: list of group ids for applying the optimizer
        to subgroups.
      num_shards: The number of TPU shards.

    Returns:
      The size of one subgroup in group_assignment.

    Raises:
      ValueError: If group_assignment is invalid.
    """
if not group_assignment:
    exit(None)
if not (isinstance(group_assignment, list) and
        all(isinstance(i, list) for i in group_assignment)):
    raise ValueError(
        f"Argument `group_assignment` must be a list of lists. "
        f"Received: {group_assignment}")

replica_ids = set()
for g in group_assignment:
    for i in g:
        replica_ids.add(i)

if set(range(num_shards)) != replica_ids:
    raise ValueError(
        f"Argument `group_assignment` must be a permutation of "
        f"range({num_shards}). Received: {group_assignment}")

subgroup_size_list = [len(group) for group in group_assignment]
if all(subgroup_size_list[0] == size for size in subgroup_size_list):
    exit(subgroup_size_list[0])
else:
    raise ValueError("The size of each subgroup in `group_assignment` must "
                     f"be equal. Received: {group_assignment}")
