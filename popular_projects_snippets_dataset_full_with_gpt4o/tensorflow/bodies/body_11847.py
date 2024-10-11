# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linalg_impl.py
"""Returns list of assertions related to `lu_reconstruct` assumptions."""
assertions = []

message = 'Input `lower_upper` must have at least 2 dimensions.'
if lower_upper.shape.rank is not None and lower_upper.shape.rank < 2:
    raise ValueError(message)
elif validate_args:
    assertions.append(
        check_ops.assert_rank_at_least_v2(lower_upper, rank=2, message=message))

message = '`rank(lower_upper)` must equal `rank(perm) + 1`'
if lower_upper.shape.rank is not None and perm.shape.rank is not None:
    if lower_upper.shape.rank != perm.shape.rank + 1:
        raise ValueError(message)
elif validate_args:
    assertions.append(
        check_ops.assert_rank(
            lower_upper, rank=array_ops.rank(perm) + 1, message=message))

message = '`lower_upper` must be square.'
if lower_upper.shape[:-2].is_fully_defined():
    if lower_upper.shape[-2] != lower_upper.shape[-1]:
        raise ValueError(message)
elif validate_args:
    m, n = array_ops.split(
        array_ops.shape(lower_upper)[-2:], num_or_size_splits=2)
    assertions.append(check_ops.assert_equal(m, n, message=message))

exit(assertions)
