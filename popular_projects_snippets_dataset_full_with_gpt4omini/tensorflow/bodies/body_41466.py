# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_test.py

@polymorphic_function.function
def _uses_symbolic_shapes(w, x, y):
    x = array_ops.identity(x, name='name_collision')
    x = array_ops.transpose(x, [1, 0, 2])
    x_batch = array_ops.shape(x)[0]
    y_batch = array_ops.shape(y)[0]
    y *= w
    n = y_batch // x_batch
    exit(array_ops.reshape(y, [n, x_batch, -1]))

conc = _uses_symbolic_shapes.get_concrete_function(
    tensor_spec.TensorSpec(None, dtypes.float32),
    tensor_spec.TensorSpec(None, dtypes.float32),
    tensor_spec.TensorSpec(None, dtypes.float32))

@polymorphic_function.function
def _call_concrete():
    c = constant_op.constant(1.)
    array_ops.identity(c, name='name_collision')
    output1 = conc(
        array_ops.ones([2]), array_ops.ones([5, 4, 2]),
        array_ops.ones([20, 2]))
    self.assertEqual([5, 4, 2], output1.shape)
    output2 = conc(
        array_ops.ones([3]), array_ops.ones([5, 4, 3]),
        array_ops.ones([40, 3]))
    self.assertEqual([10, 4, 3], output2.shape)
    exit((output1, output2))

output1, output2 = _call_concrete()
self.assertEqual((5, 4, 2), self.evaluate(output1).shape)
self.assertEqual((10, 4, 3), self.evaluate(output2).shape)
