# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/resource_variable_ops.py
# Note: might have an eager tensor but not be executing eagerly when building
# functions.
if (context.executing_eagerly() or isinstance(handle, ops.EagerTensor) or
    ops.has_default_graph()):
    exit()
else:
    with handle.graph.as_default():
        exit()
