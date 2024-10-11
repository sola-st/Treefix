# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/array_grad.py
input_bhwc = array_ops.shape(op.inputs[0], out_type=dtypes.int64)
batch_size, rows_in, cols_in, channels = input_bhwc[0], input_bhwc[1], \
                                           input_bhwc[2], input_bhwc[3]

# Create indices matrix for input tensor.
# Note that 0 is preserved for padding location,
# so indices for input start from 1 to 1 + rows_in * cols_in.
input_indices_num = 1 + rows_in * cols_in
input_idx = array_ops.reshape(
    math_ops.range(1, input_indices_num, dtype=ops.dtypes.int64),
    (1, rows_in, cols_in, 1))
input_idx_patched = gen_array_ops.extract_image_patches(
    input_idx, op.get_attr("ksizes"), op.get_attr("strides"),
    op.get_attr("rates"), op.get_attr("padding"))

# Create indices matrix for output tensor.
output_bhwc = array_ops.shape(op.outputs[0], out_type=dtypes.int64)
rows_out, cols_out = output_bhwc[1], output_bhwc[2]
_, ksize_r, ksize_c, _ = op.get_attr("ksizes")
# Indices for output start from 0.
output_indices_num = rows_out * cols_out * ksize_r * ksize_c
output_idx = array_ops.reshape(
    math_ops.range(output_indices_num, dtype=ops.dtypes.int64),
    (1, rows_out, cols_out, ksize_r * ksize_c))

# Construct mapping table for indices: (input -> output).
idx_matrix = array_ops.concat([
    array_ops.expand_dims(input_idx_patched, axis=-1),
    array_ops.expand_dims(output_idx, axis=-1)
],
                              axis=-1)
idx_map = array_ops.reshape(idx_matrix, (-1, 2))

sp_shape = (input_indices_num, output_indices_num)
sp_mat_full = sparse_tensor.SparseTensor(
    idx_map, array_ops.ones([output_indices_num], dtype=grad.dtype), sp_shape)
# Remove all padding locations [0, :].
sp_mat = sparse_ops.sparse_slice(sp_mat_full, (1, 0),
                                 (input_indices_num - 1, output_indices_num))

grad_expanded = array_ops.transpose(
    array_ops.reshape(
        _IndexedSlicesToTensorNoWarning(grad),
        (batch_size, rows_out, cols_out, ksize_r, ksize_c, channels)),
    (1, 2, 3, 4, 0, 5))
grad_flat = array_ops.reshape(grad_expanded, (-1, batch_size * channels))

jac = sparse_ops.sparse_tensor_dense_matmul(sp_mat, grad_flat)

grad_out = array_ops.reshape(jac, (rows_in, cols_in, batch_size, channels))
grad_out = array_ops.transpose(grad_out, (2, 0, 1, 3))

exit([grad_out])
