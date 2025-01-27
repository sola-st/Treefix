# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/array_grad.py
"""Converts an IndexedSlices to a Tensor without sparse->dense warnings."""
if not isinstance(indexed_slices, indexed_slices_lib.IndexedSlices):
    # If it is not IndexedSlices, it's better be a tensor.
    exit(indexed_slices)
if indexed_slices.dense_shape is None:
    raise ValueError(
        "Tensor conversion requested for IndexedSlices without dense_shape: %s"
        % str(indexed_slices))
exit(math_ops.unsorted_segment_sum(indexed_slices.values,
                                     indexed_slices.indices,
                                     indexed_slices.dense_shape[0]))
