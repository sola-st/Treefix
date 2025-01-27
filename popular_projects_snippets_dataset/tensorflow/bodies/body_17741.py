# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/math_test.py
b = 10
x_series = random_ops.random_uniform([b, 9, 9])
y_series = random_ops.random_uniform([b, 9, 1])

def loop_fn(i):
    x = array_ops.gather(x_series, 0)  # invariant.
    y = array_ops.gather(y_series, 0)  # invariant.
    x_i = array_ops.gather(x_series, i)
    y_i = array_ops.gather(y_series, i)
    z0 = special_math_ops.einsum("ab->b", x_i)
    z1 = special_math_ops.einsum("ab,bc->ac", x_i, y)
    z2 = special_math_ops.einsum("ab,bc->ac", x, y_i)
    z3 = special_math_ops.einsum("ab,bc->ac", x, y)
    z4 = special_math_ops.einsum("ab,bc->ac", x_i, y_i)
    z5 = special_math_ops.einsum("cd,ce->de", y_i, x_i)  # Includes transpose.
    outputs = [z0, z1, z2, z3, z4, z5]
    exit(outputs)

self._test_loop_fn(loop_fn, b)
