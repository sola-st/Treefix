# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator_block_lower_triangular.py
arg_dim = -1 if adjoint_arg else -2
block_dimensions = (self._block_range_dimensions() if adjoint
                    else self._block_domain_dimensions())
blockwise_arg = linear_operator_util.arg_is_blockwise(
    block_dimensions, x, arg_dim)
if blockwise_arg:
    split_x = x
else:
    split_dim = -1 if adjoint_arg else -2
    # Split input by columns if adjoint_arg is True, else rows
    split_x = linear_operator_util.split_arg_into_blocks(
        self._block_domain_dimensions(),
        self._block_domain_dimension_tensors,
        x, axis=split_dim)

result_list = []
# Iterate over row-partitions (i.e. column-partitions of the adjoint).
if adjoint:
    for index in range(len(self.operators)):
        # Begin with the operator on the diagonal and apply it to the
        # respective `rhs` block.
        result = self.operators[index][index].matmul(
            split_x[index], adjoint=adjoint, adjoint_arg=adjoint_arg)

        # Iterate top to bottom over the operators in the remainder of the
        # column-partition (i.e. left to right over the row-partition of the
        # adjoint), apply the operator to the respective `rhs` block and
        # accumulate the sum. For example, given the
        # `LinearOperatorBlockLowerTriangular`:
        #
        # op = [[A, 0, 0],
        #       [B, C, 0],
        #       [D, E, F]]
        #
        # if `index = 1`, the following loop calculates:
        # `y_1 = (C.matmul(x_1, adjoint=adjoint) +
        #         E.matmul(x_2, adjoint=adjoint)`,
        # where `x_1` and `x_2` are splits of `x`.
        for j in range(index + 1, len(self.operators)):
            result += self.operators[j][index].matmul(
                split_x[j], adjoint=adjoint, adjoint_arg=adjoint_arg)
        result_list.append(result)
else:
    for row in self.operators:
        # Begin with the left-most operator in the row-partition and apply it
        # to the first `rhs` block.
        result = row[0].matmul(
            split_x[0], adjoint=adjoint, adjoint_arg=adjoint_arg)
        # Iterate left to right over the operators in the remainder of the row
        # partition, apply the operator to the respective `rhs` block, and
        # accumulate the sum.
        for j, operator in enumerate(row[1:]):
            result += operator.matmul(
                split_x[j + 1], adjoint=adjoint, adjoint_arg=adjoint_arg)
        result_list.append(result)

if blockwise_arg:
    exit(result_list)

result_list = linear_operator_util.broadcast_matrix_batch_dims(
    result_list)
exit(array_ops.concat(result_list, axis=-2))
