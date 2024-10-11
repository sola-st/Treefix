# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/variables/resource_variable_ops_test.py
v = resource_variable_ops.ResourceVariable(1.)
self.evaluate(v.initializer)
result = nest.flatten(v, expand_composites=True)
# TODO(b/246438937): Update this to dt_resource tensor once we expand
# ResourceVariables with expand_composites=True.
self.assertIsInstance(result[0], resource_variable_ops.ResourceVariable)
