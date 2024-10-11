# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_test.py

@polymorphic_function.function
def func():
    pass

graph = func.get_concrete_function().graph
del func

# If the graph is deleted, then an exception is raised on reading `captures`
self.assertEmpty(graph.captures)
