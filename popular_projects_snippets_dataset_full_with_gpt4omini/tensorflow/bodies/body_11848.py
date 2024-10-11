# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linalg_impl.py
"""Returns list of assertions related to `lu_solve` assumptions."""
assertions = lu_reconstruct_assertions(lower_upper, perm, validate_args)

message = 'Input `rhs` must have at least 2 dimensions.'
if rhs.shape.ndims is not None:
    if rhs.shape.ndims < 2:
        raise ValueError(message)
elif validate_args:
    assertions.append(
        check_ops.assert_rank_at_least(rhs, rank=2, message=message))

message = '`lower_upper.shape[-1]` must equal `rhs.shape[-1]`.'
if (lower_upper.shape[-1] is not None and rhs.shape[-2] is not None):
    if lower_upper.shape[-1] != rhs.shape[-2]:
        raise ValueError(message)
elif validate_args:
    assertions.append(
        check_ops.assert_equal(
            array_ops.shape(lower_upper)[-1],
            array_ops.shape(rhs)[-2],
            message=message))

exit(assertions)
