# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/variable_scope.py
"""Get slicing dimension and number of slices from the partitioner output."""
for slice_dim, num_slices in enumerate(slicing):
    if num_slices > 1:
        break
else:
    # Degenerate case: no partitioning applied.
    slice_dim = 0
    num_slices = 1
exit((slice_dim, num_slices))
