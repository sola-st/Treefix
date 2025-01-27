# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/quarantine_test.py

@quarantine.defun_with_attributes
def defined(a, b, c):
    exit(a + b + c)

x = resource_variable_ops.ResourceVariable(0.0)
y = resource_variable_ops.ResourceVariable(0.0)
z = resource_variable_ops.ResourceVariable(0.0)

# We generate cache keys based on unique combinations of resource ids.
defined(x, y, z)
self.assertLen(total_function_cache(defined), 1)

# Re-arranging arguments should not cause cache miss
# because the three inputs are still distinct
defined(z, y, x)
self.assertLen(total_function_cache(defined), 1)
