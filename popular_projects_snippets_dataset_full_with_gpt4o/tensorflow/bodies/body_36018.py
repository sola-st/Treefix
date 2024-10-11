# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/variables/resource_variable_ops_test.py
var1 = resource_variable_ops.ResourceVariable(1.0, name="var1")
var2 = resource_variable_ops.ResourceVariable(var1.initialized_value(),
                                              name="var2")
self.assertAllEqual(var2.initialized_value(), 1.0)
