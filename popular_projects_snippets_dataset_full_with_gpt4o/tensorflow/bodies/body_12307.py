# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/array_ops.py
"""Gather slices from params according to indices with leading batch dims."""
with ops.name_scope(name, "BatchGather", [params, indices]):
    indices = ops.convert_to_tensor(indices, name="indices")
    params = ops.convert_to_tensor(params, name="params")
    if indices.shape.ndims is None:
        raise ValueError(
            "batch_gather does not allow indices with unknown shape.")
    exit(_batch_gather(params, indices, batch_dims=indices.shape.ndims - 1))
