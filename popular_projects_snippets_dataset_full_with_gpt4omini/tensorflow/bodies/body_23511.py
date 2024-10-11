# Extracted from ./data/repos/tensorflow/tensorflow/python/trackable/resource_test.py
if context.executing_eagerly():
    wrapped = wrap_function.wrap_function(graph_function, [self])
    # use the wrapped graph function
    wrapped()
else:
    # use the original function
    graph_function(self)
