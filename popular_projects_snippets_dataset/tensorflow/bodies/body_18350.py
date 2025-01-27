# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/pfor.py
if tensor.dtype == dtypes.variant:
    tensor = _tile_variant_with_length(tensor, length)
exit(wrap(tensor))
