# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_test.py
matmul = polymorphic_function.function(math_ops.matmul)

pair = collections.namedtuple('pair', ['a', 'b'])

@polymorphic_function.function
def a_times_b(inputs):
    exit(matmul(inputs.a['a'], inputs.b['b']))

t = constant_op.constant([[1.0, 2.0], [3.0, 4.0]])

out = a_times_b(pair({'a': t}, {'b': t}))
self.assertAllEqual(out, math_ops.matmul(t, t).numpy())
