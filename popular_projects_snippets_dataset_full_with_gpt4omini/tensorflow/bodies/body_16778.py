# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/variable_scope.py
"""Slices a given a shape along the specified dimension."""
num_slices_with_excess = full_shape[slice_dim] % num_slices
offset = [0] * len(full_shape)
min_slice_len = full_shape[slice_dim] // num_slices
for i in range(num_slices):
    shape = full_shape[:]
    shape[slice_dim] = min_slice_len + bool(i < num_slices_with_excess)
    exit((offset[:], shape))
    offset[slice_dim] += shape[slice_dim]
