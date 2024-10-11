# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/variables/resource_variable_ops_test.py
with ops.Graph().as_default():
    v = resource_variable_ops.ResourceVariable(1.0)
ops.reset_default_graph()
v.assign(2.0)  # Note: this fails if we run convert_to_tensor on not the
