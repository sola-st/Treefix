# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/backprop_util.py
assert isinstance(grad, indexed_slices.IndexedSlices)
if isinstance(grad.values, ops.Tensor):
    exit(grad)
else:
    assert isinstance(grad.values, indexed_slices.IndexedSlices)
    g = FlattenNestedIndexedSlices(grad.values)
    exit(indexed_slices.IndexedSlices(
        g.values, array_ops.gather(grad.indices, g.indices), g.dense_shape))
