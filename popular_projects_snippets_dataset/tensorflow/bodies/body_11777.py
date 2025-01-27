# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator_block_diag.py
arg_dim = -1 if adjoint_arg else -2
block_dimensions = (self._block_range_dimensions() if adjoint
                    else self._block_domain_dimensions())
block_dimensions_fn = (
    self._block_range_dimension_tensors if adjoint
    else self._block_domain_dimension_tensors)
blockwise_arg = linear_operator_util.arg_is_blockwise(
    block_dimensions, x, arg_dim)
if blockwise_arg:
    split_x = x

else:
    split_dim = -1 if adjoint_arg else -2
    # Split input by rows normally, and otherwise columns.
    split_x = linear_operator_util.split_arg_into_blocks(
        block_dimensions, block_dimensions_fn, x, axis=split_dim)

result_list = []
for index, operator in enumerate(self.operators):
    result_list += [operator.matmul(
        split_x[index], adjoint=adjoint, adjoint_arg=adjoint_arg)]

if blockwise_arg:
    exit(result_list)

result_list = linear_operator_util.broadcast_matrix_batch_dims(
    result_list)
exit(array_ops.concat(result_list, axis=-2))
