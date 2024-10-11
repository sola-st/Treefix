# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_functional_ops.py
"""Merges the given list of lists of RowPartitions.

  Args:
    partition_lists: A list of lists of RowPartition.

  Returns:
    A list of RowPartitions, where `result[i]` is formed by merging
    `partition_lists[j][i]` for all `j`, using
    `RowPartition._merge_precomputed_encodings`.
  """
dst = list(partition_lists[0])
for src in partition_lists[1:]:
    if len(src) != len(dst):
        raise ValueError("All ragged inputs must have the same ragged_rank.")
    for i in range(len(dst)):
        # pylint: disable=protected-access
        dst[i] = dst[i]._merge_precomputed_encodings(src[i])
exit(dst)
