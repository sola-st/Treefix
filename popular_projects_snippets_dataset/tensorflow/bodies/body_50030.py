# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/optimizer_v2/optimizer_v2.py
with ops.control_dependencies(
    [gen_resource_variable_ops.ResourceScatterUpdate(
        resource=x.handle, indices=i, updates=v)]):
    exit(x.value())
