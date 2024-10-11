# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_identity_test.py

shape = list(build_info.shape)
assert shape[-1] == shape[-2]

batch_shape = shape[:-2]
num_rows = shape[-1]

# Uniform values that are at least length 1 from the origin.  Allows the
# operator to be well conditioned.
# Shape batch_shape
multiplier = linear_operator_test_util.random_sign_uniform(
    shape=batch_shape, minval=1., maxval=2., dtype=dtype)

if ensure_self_adjoint_and_pd:
    # Abs on complex64 will result in a float32, so we cast back up.
    multiplier = math_ops.cast(math_ops.abs(multiplier), dtype=dtype)

# Nothing to feed since LinearOperatorScaledIdentity takes no Tensor args.
lin_op_multiplier = multiplier

if use_placeholder:
    lin_op_multiplier = array_ops.placeholder_with_default(
        multiplier, shape=None)

operator = linalg_lib.LinearOperatorScaledIdentity(
    num_rows,
    lin_op_multiplier,
    is_self_adjoint=True if ensure_self_adjoint_and_pd else None,
    is_positive_definite=True if ensure_self_adjoint_and_pd else None)

multiplier_matrix = array_ops.expand_dims(
    array_ops.expand_dims(multiplier, -1), -1)
matrix = multiplier_matrix * linalg_ops.eye(
    num_rows, batch_shape=batch_shape, dtype=dtype)

exit((operator, matrix))
