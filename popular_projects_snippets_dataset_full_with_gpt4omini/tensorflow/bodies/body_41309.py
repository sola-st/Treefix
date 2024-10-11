# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_test.py
self.v = resource_variable_ops.ResourceVariable(
    lambda: constant_op.constant(2.0))
exit(self.v.read_value())
