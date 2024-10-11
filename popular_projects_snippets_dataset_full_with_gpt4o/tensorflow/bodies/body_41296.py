# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_test.py
matmul = polymorphic_function.function(math_ops.matmul)

pair = collections.namedtuple('pair', ['a', 'b'])

@polymorphic_function.function
def a_times_b(inputs):
    exit(matmul(inputs.a['a'], inputs.b['b']))

t = constant_op.constant([[1.0, 2.0], [3.0, 4.0]])
sq_op = a_times_b.get_concrete_function(
    pair(
        dict(a=tensor_spec.TensorSpec([2, 2], dtypes.float32, 'a')),
        dict(b=tensor_spec.TensorSpec([2, 2], dtypes.float32, 'b'))))
self.assertEqual(sq_op.output_shapes, tensor_shape.TensorShape([2, 2]))
out = sq_op(a=t, b=t)
self.assertAllEqual(out, math_ops.matmul(t, t).numpy())
