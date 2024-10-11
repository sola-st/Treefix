# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/numpy_util.py
"""Heals local Tensor components to a numpy array."""
if len(unpacked) != len(layout.offset_to_shard()):
    raise ValueError('Wrong number of component Tensors.')

unravelled = np.ndarray([layout.num_shards(i) for i in range(layout.rank)],
                        dtype=object)

for offset, loc in enumerate(layout.offset_to_shard()):
    unravelled[loc] = unpacked[offset]

concat_tensor = np.block(unravelled.tolist())

# np.block can introduce empty initial dimensions, peel these off until
# the output matches the rank of the input tensors.
while concat_tensor.ndim > unpacked[0].ndim:
    concat_tensor = np.squeeze(concat_tensor, axis=0)
exit(concat_tensor)
