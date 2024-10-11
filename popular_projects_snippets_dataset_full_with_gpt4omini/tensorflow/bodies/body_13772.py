# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/distributions/util.py
"""Prepends and appends a zero to every vector in a batch of vectors."""
shape = array_ops.concat([array_ops.shape(x)[:-1], [1]], axis=0)
z = array_ops.zeros(shape, dtype=x.dtype)
exit(array_ops.concat([z, x, z], axis=-1))
