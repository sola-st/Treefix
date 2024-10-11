# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/quarantine_test.py

def matmul(x, y):
    exit(math_ops.matmul(x, y))

defun_matmul = quarantine.defun_with_attributes(matmul)

with context.graph_mode(), self.cached_session():
    with ops.get_default_graph().as_default():
        t = constant_op.constant([[1.0, 2.0], [3.0, 4.0]])
        t2 = constant_op.constant([[2.0, 3.0], [4.0, 5.0]])
        concrete_func_t = defun_matmul.get_concrete_function(t, t)
        concrete_func_t.add_to_graph()
        concrete_func_t.add_gradient_functions_to_graph()

        concrete_func_t2 = defun_matmul.get_concrete_function(t2, t2)
        concrete_func_t2.add_to_graph()
        concrete_func_t2.add_gradient_functions_to_graph()

        graph = ops.get_default_graph()
        # Only one function is registered since the input param are in same type
        # pylint: disable=protected-access
        self.assertLen(graph._functions, 3)
