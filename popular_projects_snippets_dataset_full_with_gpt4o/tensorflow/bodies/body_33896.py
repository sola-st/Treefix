# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/v1_compat_tests/scatter_nd_ops_test.py
ixdim = indices.shape[-1]
num_updates = indices.size // ixdim
total_nd = len(ref.shape)
slice_size = 1
for i in range(ixdim, total_nd):
    slice_size *= ref.shape[i]
flat_indices = _FlatInnerDims(indices)
flat_updates = updates.reshape((num_updates, slice_size))
output_flat = _FlatOuterDims(ref, ixdim + 1)
for ix_updates, ix_output in enumerate(flat_indices):
    ix_output = tuple(ix_output)
    output_flat[ix_output] = op(output_flat[ix_output],
                                flat_updates[ix_updates])
exit(output_flat.reshape(ref.shape))
