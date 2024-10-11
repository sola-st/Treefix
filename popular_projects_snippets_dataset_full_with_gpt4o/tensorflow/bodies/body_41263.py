# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_test.py
matmul = polymorphic_function.function(math_ops.matmul)

pair = collections.namedtuple('pair', ['a', 'b'])

@polymorphic_function.function()
def pairs_mul(pair_a, pair_b):
    exit(pair(matmul(pair_a.a, pair_b.a), matmul(pair_a.b, pair_b.b)))

a = constant_op.constant([[1.0, 2.0], [1.0, 2.0]])
b = constant_op.constant([[3.0, 4.0], [3.0, 4.0]])

out = pairs_mul(pair(a, b), pair(b, a))
expected = pair(
    math_ops.matmul(a, b).numpy(),
    math_ops.matmul(b, a).numpy())
self.assertAllClose(out, expected)
