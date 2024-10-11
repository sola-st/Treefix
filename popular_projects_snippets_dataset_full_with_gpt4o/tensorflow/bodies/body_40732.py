# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/quarantine_test.py

def matmul(x, y):
    exit(math_ops.matmul(x, y))

defun_matmul = quarantine.defun_with_attributes(
    matmul,
    input_signature=[
        tensor_spec.TensorSpec(shape=(2, 2), dtype=dtypes.float32),
        tensor_spec.TensorSpec(shape=(2, 2), dtype=dtypes.float32)
    ])
with context.graph_mode(), self.cached_session():
    with ops.get_default_graph().as_default():
        t = constant_op.constant([[1.0, 2.0], [3.0, 4.0]])
        concrete_func = defun_matmul.get_concrete_function(t, t)
        concrete_func.add_to_graph()
        concrete_func.add_gradient_functions_to_graph()

        graph = ops.get_default_graph()
        # pylint: disable=protected-access
        self.assertLen(graph._functions, 3)

        # Test register function with cache, note inputs are ignored.
        concrete_func = defun_matmul.get_concrete_function()
        concrete_func.add_to_graph()
        concrete_func.add_gradient_functions_to_graph()
        graph = ops.get_default_graph()
        self.assertLen(graph._functions, 3)
