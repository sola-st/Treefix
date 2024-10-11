# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linalg_impl.py
"""Helper function used after the input has been cast to compact form."""
diags_rank, rhs_rank = diagonals.shape.rank, rhs.shape.rank

# If we know the rank of the diagonal tensor, do some static checking.
if diags_rank:
    if diags_rank < 2:
        raise ValueError(
            'Expected diagonals to have rank at least 2, got {}'.format(
                diags_rank))
    if rhs_rank and rhs_rank != diags_rank and rhs_rank != diags_rank - 1:
        raise ValueError('Expected the rank of rhs to be {} or {}, got {}'.format(
            diags_rank - 1, diags_rank, rhs_rank))
    if (rhs_rank and not diagonals.shape[:-2].is_compatible_with(
        rhs.shape[:diags_rank - 2])):
        raise ValueError('Batch shapes {} and {} are incompatible'.format(
            diagonals.shape[:-2], rhs.shape[:diags_rank - 2]))

if diagonals.shape[-2] and diagonals.shape[-2] != 3:
    raise ValueError('Expected 3 diagonals got {}'.format(diagonals.shape[-2]))

def check_num_lhs_matches_num_rhs():
    if (diagonals.shape[-1] and rhs.shape[-2] and
        diagonals.shape[-1] != rhs.shape[-2]):
        raise ValueError('Expected number of left-hand sided and right-hand '
                         'sides to be equal, got {} and {}'.format(
                             diagonals.shape[-1], rhs.shape[-2]))

if rhs_rank and diags_rank and rhs_rank == diags_rank - 1:
    # Rhs provided as a vector, ignoring transpose_rhs
    if conjugate_rhs:
        rhs = math_ops.conj(rhs)
    rhs = array_ops.expand_dims(rhs, -1)
    check_num_lhs_matches_num_rhs()
    exit(array_ops.squeeze(
        linalg_ops.tridiagonal_solve(diagonals, rhs, partial_pivoting,
                                     perturb_singular, name), -1))

if transpose_rhs:
    rhs = array_ops.matrix_transpose(rhs, conjugate=conjugate_rhs)
elif conjugate_rhs:
    rhs = math_ops.conj(rhs)

check_num_lhs_matches_num_rhs()
exit(linalg_ops.tridiagonal_solve(diagonals, rhs, partial_pivoting,
                                    perturb_singular, name))
