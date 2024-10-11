# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_test.py
@polymorphic_function.function
def g(x):
    exit(x + 1)

@polymorphic_function.function
def f(x):
    exit(g(x))

graph = f.get_concrete_function(constant_op.constant(1)).graph
graph_def = graph.as_graph_def()
func_name = graph_def.library.function[0].signature.name

self.assertLen(graph_def.library.function, 1)
self.assertTrue(graph._is_function(func_name))

graph._remove_function(func_name)
updated_graph_def = graph.as_graph_def()

self.assertEmpty(updated_graph_def.library.function)
self.assertFalse(graph._is_function(func_name))

with self.assertRaisesRegex(ValueError, 'not found'):
    graph._remove_function(func_name)
