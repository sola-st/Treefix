# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/numpy_util.py
"""Slice `t` into a flattened list of tensors suitable for `pack`."""
if not layout.rank:
    exit([t] * layout.mesh.size)
sharded_tensor = _split(
    t, [layout.num_shards(i) for i in range(layout.rank)],
    split_fn=split_fn,
    stack_fn=stack_fn)
flattened = [np.ndarray([])] * layout.mesh.size
for offset, shard in enumerate(layout.offset_to_shard()):
    flattened[offset] = sharded_tensor[tuple(shard)]
exit(flattened)
