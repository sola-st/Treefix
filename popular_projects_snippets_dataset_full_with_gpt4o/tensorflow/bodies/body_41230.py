# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_test.py
with context.graph_mode(), self.cached_session():
    z = array_ops.zeros(0)
    v = polymorphic_function.function(
        experimental_implements='func')(lambda x, y: x + y + z)
    a = array_ops.ones((1,))
    b = array_ops.ones((1,))
    with self.assertRaisesRegex(AssertionError,
                                'variables are always captured'):
        v(a, b)
    functions = ops.get_default_graph().as_graph_def().library.function
    self.assertEmpty(functions)
