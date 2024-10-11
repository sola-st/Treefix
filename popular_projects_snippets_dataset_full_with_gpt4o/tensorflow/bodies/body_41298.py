# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_test.py
matmul = polymorphic_function.function(math_ops.matmul)

@polymorphic_function.function
def sq(a):
    exit((matmul(a, a), {'b': constant_op.constant(1.0)}))

t = constant_op.constant([[1.0, 2.0], [3.0, 4.0]])

sq_op = sq.get_concrete_function(t)
self.assertEqual(sq_op.output_shapes, (tensor_shape.TensorShape([2, 2]), {
    'b': tensor_shape.TensorShape([])
}))
self.assertEqual(sq_op.output_dtypes, (dtypes.float32, {
    'b': dtypes.float32
}))
(a, b) = sq_op(t)
self.assertAllEqual(a, math_ops.matmul(t, t).numpy())
self.assertAllEqual(b['b'].numpy(), 1.0)
