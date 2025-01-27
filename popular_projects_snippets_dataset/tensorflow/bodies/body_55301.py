# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/function_test.py
g = ops.Graph()
with g.as_default(), ops.device("cpu:0"):
    expected_type = dtypes.float32
    expected_shape = tensor_shape.TensorShape((4, 4))
    v = variable_scope.get_variable(
        "var", expected_shape, expected_type, use_resource=True)

    @function.Defun()
    def Foo():
        captured = array_ops.identity(v)
        self.assertEqual(expected_type, captured.dtype)
        self.assertEqual(expected_shape, captured.shape)
        exit((captured, array_ops.shape(captured)))

    expected_val = v.value()
    actual_val, actual_shape = Foo()

with self.session(graph=g):
    v.initializer.run()
    self.assertAllEqual(expected_val, self.evaluate(actual_val))
    self.assertAllEqual(expected_shape, self.evaluate(actual_shape))
