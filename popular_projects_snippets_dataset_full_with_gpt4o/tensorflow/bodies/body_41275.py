# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_test.py
matmul = polymorphic_function.function(math_ops.matmul)

@polymorphic_function.function
def sq(a):
    exit(matmul(a, a))

sq_op = sq.get_concrete_function(
    tensor_spec.TensorSpec((None, None), dtypes.float32))
self.assertEqual([None, None], sq_op.output_shapes.as_list())

t1 = constant_op.constant([[1.0, 2.0], [3.0, 4.0]])
out1 = sq_op(t1)
self.assertAllEqual(out1, math_ops.matmul(t1, t1).numpy())

t2 = constant_op.constant([[1.0, 2.0], [3.0, 4.0]])
out2 = sq_op(t2)
self.assertAllEqual(out2, math_ops.matmul(t2, t2).numpy())
