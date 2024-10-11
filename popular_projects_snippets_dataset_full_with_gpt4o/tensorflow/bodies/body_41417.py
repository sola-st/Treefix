# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_test.py

@polymorphic_function.function
def py_add(x, y):
    exit(math_ops.add(x, y))

py_add(array_ops.ones([]), array_ops.ones([]))
add = py_add.get_concrete_function(
    tensor_spec.TensorSpec(None, dtypes.float32),
    tensor_spec.TensorSpec(None, dtypes.float32))

@polymorphic_function.function
def py_composite(x, y):
    exit((x, add(x, y)))

py_composite(array_ops.ones([]), array_ops.ones([]))
composite = py_composite.get_concrete_function(
    tensor_spec.TensorSpec(None, dtypes.float32),
    tensor_spec.TensorSpec(None, dtypes.float32))

with context.graph_mode(), self.cached_session():
    with ops.get_default_graph().as_default():
        t = constant_op.constant([[1.0, 2.0], [3.0, 4.0]])
        composite.add_to_graph()
        composite.add_gradient_functions_to_graph()

        graph = ops.get_default_graph()
        # pylint: disable=protected-access
        self.assertLen(graph._functions, 6)
        # two sets of functions, each of them are (inference, forward, backward)
        functions = list(graph._functions.values())
        captured_function_names = [
            f.definition.signature.name for f in functions
        ]
        expected_func_name_regex = [
            '.*inference.*py_composite.*',
            '.*inference.*py_add.*',
            '.*forward.*py_composite.*',
            '.*forward.*py_add.*',
            '.*inference.*backward.*py_composite.*',
            '.*inference.*backward.*py_add.*',
        ]
        for expected, found in zip(expected_func_name_regex,
                                   captured_function_names):
            self.assertRegex(found, expected)

        composite_t, composite_double = composite(t, t)
        double = add(t, t)
        self.assertAllEqual([[2, 4], [6, 8]], self.evaluate(double))
        self.assertAllEqual([[2, 4], [6, 8]], self.evaluate(composite_double))
        self.assertAllEqual([[1, 2], [3, 4]], self.evaluate(composite_t))
        # Make sure the pre registered function is used, and no other function
        # is added.
        self.assertLen(graph._functions, 6)
