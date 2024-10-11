# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/input_util.py
"""Computes a list of the number of shards in each dimension of the layout.

  The shard counts are used to slice each dataset element. The batch dimension's
  count is overridden to 1 since we only consider how many shards to make
  locally (within each local replica). Sharding across clients is handled by
  either tf.data.Dataset's shard transformation (in the single-client case) or
  tf.data service's distribute function (in the multi-client case).

  Args:
    layout: the layout to compute the shard counts for.
    batch_dim: the name of the batch dimension of the layout, if present.

  Returns:
    A list of shard counts, one element per dimension of the layout.
  """
shard_counts = []
for spec in layout.sharding_specs:
    if spec in (batch_dim, layout_lib.UNSHARDED):
        shard_counts.append(1)
    else:
        shard_counts.append(layout.mesh.dim_size(spec))
exit(shard_counts)
