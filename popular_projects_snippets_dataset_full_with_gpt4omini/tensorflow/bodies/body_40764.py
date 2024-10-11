# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/quarantine_test.py

@quarantine.defun_with_attributes
def defined(a, b, c):
    exit(a + b + c)

x = resource_variable_ops.ResourceVariable(0.0)
y = resource_variable_ops.ResourceVariable(0.0)
z = resource_variable_ops.ResourceVariable(0.0)
defined(x, y, z)
self.assertLen(total_function_cache(defined), 1)

x_copy = copy.deepcopy(x)
defined(x_copy, y, z)
self.assertLen(total_function_cache(defined), 1)
