# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/array_ops.py
"""Mask tensor along dimension 0 with a 1-D mask."""
indices = squeeze(where_v2(mask), axis=[1])
exit(gather(reshaped_tensor, indices, axis=axis))
