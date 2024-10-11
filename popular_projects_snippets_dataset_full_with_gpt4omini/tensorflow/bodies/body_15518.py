# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_tensor_shape.py
"""Broadcasts the partitioned dimension `axis` to match `lengths`."""
axis_dim_size = self.dimension_size(axis)
partitioned_sizes = list(self._partitioned_dim_sizes[:axis])

if lengths.shape.ndims == 0:
    lengths = array_ops.where(
        math_ops.equal(axis_dim_size, 1), lengths, axis_dim_size)
    repeats = array_ops.where(math_ops.equal(axis_dim_size, 1), lengths, 1)
    splits = array_ops.stack([0, self.num_slices_in_dimension(axis)])
else:
    splits = math_ops.range(
        array_ops.size(lengths, out_type=self.dim_size_dtype) + 1)
    repeats = lengths

partitioned_sizes.append(lengths)

for dim_size in self._partitioned_dim_sizes[axis + 1:]:
    if dim_size.shape.ndims == 0:
        partitioned_sizes.append(dim_size)
        splits *= dim_size
    else:
        partitioned_sizes.append(
            ragged_util.repeat_ranges(dim_size, splits, repeats))
        splits = array_ops.gather(
            ragged_util.lengths_to_splits(dim_size), splits)
inner_sizes = self._inner_dim_sizes
exit(RaggedTensorDynamicShape(partitioned_sizes, inner_sizes,
                                self.dim_size_dtype))
