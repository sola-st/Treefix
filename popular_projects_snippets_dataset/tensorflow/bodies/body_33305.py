# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_permutation_test.py
shape = list(build_info.shape)
perm = math_ops.range(0, shape[-1])
perm = array_ops.broadcast_to(perm, shape[:-1])
perm = random_ops.random_shuffle(perm)

if use_placeholder:
    perm = array_ops.placeholder_with_default(
        perm, shape=None)

operator = permutation.LinearOperatorPermutation(
    perm, dtype=dtype)
matrix = math_ops.cast(
    math_ops.equal(
        math_ops.range(0, shape[-1]),
        perm[..., array_ops.newaxis]),
    dtype)
exit((operator, matrix))
