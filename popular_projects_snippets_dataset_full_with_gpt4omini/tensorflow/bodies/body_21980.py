# Extracted from ./data/repos/tensorflow/tensorflow/python/training/adam.py
with ops.control_dependencies(
    [resource_variable_ops.resource_scatter_add(x.handle, i, v)]):
    exit(x.value())
