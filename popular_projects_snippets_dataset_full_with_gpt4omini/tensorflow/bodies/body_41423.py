# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_test.py
self.skipTest('b/209081027: Enable this test after Variable becomes a '
              'CompositeTensor and Variable gets expand to handle tensor.')

@polymorphic_function.function
def foo(v1, v2):
    exit(v1 + v2)

v1 = resource_variable_ops.ResourceVariable(1.0)
v2 = resource_variable_ops.ResourceVariable(2.0)
graph_function = foo.get_concrete_function(v1, v1)
self.assertAllEqual(graph_function(v1, v1), 2.0)
with self.assertRaises(TypeError):
    graph_function(v1, v2)
