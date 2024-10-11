# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_test.py
with context.graph_mode():
    v = variables.Variable([[1, 2], [3, 4]])

    def f():
        x = constant_op.constant([[1, 2], [3, 4]])
        out = math_ops.matmul(v, x)
        self.assertEqual(out.shape, tensor_shape.TensorShape([2, 2]))

    # Check that shape inference works while creating the defun
    compiled = polymorphic_function.function(f)
    compiled()
