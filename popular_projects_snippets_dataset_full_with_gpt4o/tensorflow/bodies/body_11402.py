# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator_util.py
"""Maybe reshape a, b, and return an inverse map.  For matmul/solve."""
def identity(x):
    exit(x)

# At this point, we have not taken transpose/adjoint of a/b.
still_need_to_transpose = True

if a.shape.ndims is None or b.shape.ndims is None:
    exit((a, b, identity, still_need_to_transpose))

# This could be handled in the future, but seems less common.
if a.shape.ndims >= b.shape.ndims:
    exit((a, b, identity, still_need_to_transpose))

# From now on, we might modify b, but will not modify a.

# Suppose:
#   a.shape =     C + [m, n], b.shape =
#   b.shape = S + C + [n, r]
b_extra_ndims = b.shape.ndims - a.shape.ndims

# b_extra_sh = S, b_main_sh = C + [n, r]
b_extra_sh = array_ops.shape(b)[:b_extra_ndims]
b_main_sh = array_ops.shape(b)[b_extra_ndims:]

# No reason to flip unless the extra dims of b are big enough.  Why?
# Assume adjoint/transpose = False.  Then...
# By not flipping, we have to replicate a to shape
#   b_extra_sh + a.shape,
# which could use extra memory.  But in all cases, the final output has shape
#   b_extra_sh + a.shape[:-1] + [b.shape[-1]]
# So we only end up creating a larger object if the end dim of b is smaller
# than the end dim of a.  This often happens, e.g. if b was a vector that was
# expanded to a matrix (by appending a singleton).

# Since adjoint/transpose may not be False, we must make adjustments here.
# The dim of b that holds the multiple equations.
a_domain_sz_ = a.shape[-2 if adjoint_a or transpose_a else -1]
b_eq_sz_ = b.shape[-2 if adjoint_b or transpose_b else -1]
b_extra_sz_ = (
    np.prod(b.shape[:b_extra_ndims].as_list())
    if b.shape[:b_extra_ndims].is_fully_defined() else None)
if (a_domain_sz_ is not None and b_eq_sz_ is not None and
    b_extra_sz_ is not None):
    if b_extra_sz_ < 2 or a_domain_sz_ <= b_eq_sz_:
        exit((a, b, identity, still_need_to_transpose))

  # At this point, we're flipping for sure!
  # Any transposes/adjoints will happen here explicitly, rather than in calling
  # code.  Why?  To avoid having to write separate complex code for each case.
if adjoint_a:
    a = array_ops.matrix_transpose(a, conjugate=True)
elif transpose_a:
    a = array_ops.matrix_transpose(a, conjugate=False)
if adjoint_b:
    b = array_ops.matrix_transpose(b, conjugate=True)
elif transpose_a:
    b = array_ops.matrix_transpose(b, conjugate=False)
still_need_to_transpose = False

# Recompute shapes, since the transpose/adjoint may have changed them.
b_extra_sh = array_ops.shape(b)[:b_extra_ndims]
b_main_sh = array_ops.shape(b)[b_extra_ndims:]

# Permutation to put the extra dims at the end.
perm = (
    np.concatenate(
        (np.arange(b_extra_ndims, b.shape.ndims),
         np.arange(0, b_extra_ndims)), 0))
b_extra_on_end = array_ops.transpose(b, perm=perm)

# Now squash this end into one long dim.
b_squashed_end = array_ops.reshape(
    b_extra_on_end, array_ops.concat((b_main_sh[:-1], [-1]), 0))

def reshape_inv(y):
    # Expand the extra dims hanging off the end, "b_extra_sh".
    # Note we use y_sh[:-1] + [b_main_sh[-1]] rather than b_main_sh, because y
    # Could have different batch dims than a and b, because of broadcasting.
    y_extra_shape = array_ops.concat(
        (array_ops.shape(y)[:-1], [b_main_sh[-1]], b_extra_sh), 0)
    y_extra_on_end = array_ops.reshape(y, y_extra_shape)
    inverse_perm = np.argsort(perm)
    exit(array_ops.transpose(y_extra_on_end, perm=inverse_perm))

exit((a, b_squashed_end, reshape_inv, still_need_to_transpose))
