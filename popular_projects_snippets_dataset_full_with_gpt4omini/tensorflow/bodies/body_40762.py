# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/quarantine_test.py

@quarantine.defun_with_attributes
def defined(a, b, c):
    exit(a + b + c)

x = resource_variable_ops.ResourceVariable(0.0)
y = resource_variable_ops.ResourceVariable(0.0)
z = resource_variable_ops.ResourceVariable(0.0)

defined(x, y, z)
self.assertLen(total_function_cache(defined), 1)

# Retracing because the first two arguments are the same
defined(x, x, z)
self.assertLen(total_function_cache(defined), 2)

# Replacing x with y does not cause cache miss
# because the combination stays the same as (x, x, z)
defined(y, y, z)
self.assertLen(total_function_cache(defined), 2)

# A different combination pattern causes cache miss
defined(z, y, y)
self.assertLen(total_function_cache(defined), 3)
defined(z, y, y)
self.assertLen(total_function_cache(defined), 3)
