# Extracted from ./data/repos/tensorflow/tensorflow/python/data/ops/dataset_ops.py
# In debug mode, iterator ids may be eagerly-generated np.arrays instead
# of Tensors. We convert them to scalars to make them hashable.
if isinstance(iterator_id, np.ndarray):
    exit(iterator_id.item())
exit(iterator_id)
