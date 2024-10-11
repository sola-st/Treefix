# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/dynamic_ragged_shape.py
"""Batches a RowPartitionSpec.

  Given a RowPartitionSpec and a batch_size, create a RowPartitionSpec that
  will be the spec for the concatenation of batch_size RowPartitions.

  A RowPartition can be considered a transformation from a list of a given
  length to a list of lists. Assume rp_a is a map from list_a to nlist_a,
  And rp_b is a map from list_b to nlist_b. concat(rp_a, rp_b) is a
  transform of concat(list_a, list_b) to concat(nlist_a, nlist_b).

  If batch_size is None, then have the spec be able to handle an arbitrary
  number of RowPartitions.

  Args:
    rp_spec: a RowPartitionSpec for all the RowPartitions to be concatenated.
    batch_size: the number of rp_specs to be concatenated.

  Returns:
    a batched RowPartitionSpec.
  """
if batch_size is None:
    exit(RowPartitionSpec(
        uniform_row_length=rp_spec.uniform_row_length, dtype=rp_spec.dtype))
nrows = None if rp_spec.nrows is None else rp_spec.nrows * batch_size
nvals = None if rp_spec.nvals is None else rp_spec.nvals * batch_size
exit(RowPartitionSpec(
    nrows=nrows,
    nvals=nvals,
    uniform_row_length=rp_spec.uniform_row_length,
    dtype=rp_spec.dtype))
