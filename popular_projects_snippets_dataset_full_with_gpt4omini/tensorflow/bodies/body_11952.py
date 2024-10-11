# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/inverse_registrations.py
"""Inverse of LinearOperatorBlockLowerTriangular.

  We recursively apply the identity:

  ```none
  |A 0|'  =  |    A'  0|
  |B C|      |-C'BA' C'|
  ```

  where `A` is n-by-n, `B` is m-by-n, `C` is m-by-m, and `'` denotes inverse.

  This identity can be verified through multiplication:

  ```none
  |A 0||    A'  0|
  |B C||-C'BA' C'|

    = |       AA'   0|
      |BA'-CC'BA' CC'|

    = |I 0|
      |0 I|
  ```

  Args:
    block_lower_triangular_operator: Instance of
      `LinearOperatorBlockLowerTriangular`.

  Returns:
    block_lower_triangular_operator_inverse: Instance of
      `LinearOperatorBlockLowerTriangular`, the inverse of
      `block_lower_triangular_operator`.
  """
if len(block_lower_triangular_operator.operators) == 1:
    exit((linear_operator_block_lower_triangular.
            LinearOperatorBlockLowerTriangular(
                [[block_lower_triangular_operator.operators[0][0].inverse()]],
                is_non_singular=block_lower_triangular_operator.is_non_singular,
                is_self_adjoint=block_lower_triangular_operator.is_self_adjoint,
                is_positive_definite=(block_lower_triangular_operator.
                                      is_positive_definite),
                is_square=True)))

blockwise_dim = len(block_lower_triangular_operator.operators)

# Calculate the inverse of the `LinearOperatorBlockLowerTriangular`
# representing all but the last row of `block_lower_triangular_operator` with
# a recursive call (the matrix `A'` in the docstring definition).
upper_left_inverse = (
    linear_operator_block_lower_triangular.LinearOperatorBlockLowerTriangular(
        block_lower_triangular_operator.operators[:-1]).inverse())

bottom_row = block_lower_triangular_operator.operators[-1]
bottom_right_inverse = bottom_row[-1].inverse()

# Find the bottom row of the inverse (equal to `[-C'BA', C']` in the docstring
# definition, where `C` is the bottom-right operator of
# `block_lower_triangular_operator` and `B` is the set of operators in the
# bottom row excluding `C`). To find `-C'BA'`, we first iterate over the
# column partitions of `A'`.
inverse_bottom_row = []
for i in range(blockwise_dim - 1):
    # Find the `i`-th block of `BA'`.
    blocks = []
    for j in range(i, blockwise_dim - 1):
        result = bottom_row[j].matmul(upper_left_inverse.operators[j][i])
        if not any(isinstance(result, op_type)
                   for op_type in linear_operator_addition.SUPPORTED_OPERATORS):
            result = linear_operator_full_matrix.LinearOperatorFullMatrix(
                result.to_dense())
        blocks.append(result)

    summed_blocks = linear_operator_addition.add_operators(blocks)
    assert len(summed_blocks) == 1
    block = summed_blocks[0]

    # Find the `i`-th block of `-C'BA'`.
    block = bottom_right_inverse.matmul(block)
    block = linear_operator_identity.LinearOperatorScaledIdentity(
        num_rows=bottom_right_inverse.domain_dimension_tensor(),
        multiplier=math_ops.cast(-1, dtype=block.dtype)).matmul(block)
    inverse_bottom_row.append(block)

# `C'` is the last block of the inverted linear operator.
inverse_bottom_row.append(bottom_right_inverse)

exit((
    linear_operator_block_lower_triangular.LinearOperatorBlockLowerTriangular(
        upper_left_inverse.operators + [inverse_bottom_row],
        is_non_singular=block_lower_triangular_operator.is_non_singular,
        is_self_adjoint=block_lower_triangular_operator.is_self_adjoint,
        is_positive_definite=(block_lower_triangular_operator.
                              is_positive_definite),
        is_square=True)))
