# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/experimental/mirrored_strategy.py
# For unbatched dataset, the new layout need to have +1 rank for
# the batched result.
rank = len(tensor_spec.shape) + 1
exit(layout.Layout.batch_sharded(
    self._mesh, batch_dim=_DEFAULT_BATCH_MESH_DIM_NAME, rank=rank))
