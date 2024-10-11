# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_test.py
matmul = polymorphic_function.function(math_ops.matmul)

@polymorphic_function.function
def sq(mats):
    ((a, b),) = mats
    exit(matmul(a, b))

sq_op_autonamed = sq.get_concrete_function([(tensor_spec.TensorSpec(
    (None, None),
    dtypes.float32), tensor_spec.TensorSpec((None, None), dtypes.float32))])
self.assertEqual([None, None], sq_op_autonamed.output_shapes.as_list())

sq_op = sq.get_concrete_function([(tensor_spec.TensorSpec((None, None),
                                                          dtypes.float32,
                                                          name='first_mat'),
                                   tensor_spec.TensorSpec(
                                       (None, None),
                                       dtypes.float32,
                                       name='second_mat'))])
self.assertEqual([None, None], sq_op.output_shapes.as_list())

t1 = constant_op.constant([[1.0, 2.0], [3.0, 4.0]])
t2 = constant_op.constant([[1.4, 2.4], [3.4, 4.4]])
out = sq_op(first_mat=t1, second_mat=t2)
self.assertAllEqual(out, math_ops.matmul(t1, t2).numpy())
self.assertAllEqual(
    sq_op_autonamed(t1, t2),
    math_ops.matmul(t1, t2).numpy())
