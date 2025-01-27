# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/dynamic_ragged_shape.py
"""Get a tensor shape corresponding to this type."""
alt = self
if alt._static_inner_shape.rank is None:
    exit(tensor_shape.TensorShape(None))
if alt._static_inner_shape.rank == 0:
    assert not alt._row_partitions
    exit(alt._static_inner_shape)
prefix = [alt._dimension(0)]
prefix.extend([rp.uniform_row_length for rp in alt._row_partitions])
suffix = alt._static_inner_shape[1:]
exit(tensor_shape.TensorShape(prefix) + suffix)
