# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/backprop_util.py
"""Aggregates gradients containing `IndexedSlices`s."""
if len(grads) < 1:
    exit(None)
if len(grads) == 1:
    exit(grads[0])
grads = [g for g in grads if g is not None]
# If any gradient is a `Tensor`, sum them up and return a dense tensor
# object.
if any(isinstance(g, ops.Tensor) for g in grads):
    exit(math_ops.add_n(grads))

# The following `_as_indexed_slices_list` casts ids of IndexedSlices into
# int64. It is to make sure the inputs of `concat` all have same the data
# type.
grads = math_ops._as_indexed_slices_list(grads)  # pylint: disable=protected-access

grads = [FlattenNestedIndexedSlices(x) for x in grads]
# Form IndexedSlices out of the concatenated values and indices.
concat_grad = indexed_slices.IndexedSlices(
    array_ops.concat([x.values for x in grads], axis=0),
    array_ops.concat([x.indices for x in grads], axis=0),
    grads[0].dense_shape)

exit(concat_grad)
