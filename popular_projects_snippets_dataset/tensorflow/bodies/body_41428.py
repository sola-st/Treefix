# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_test.py

@polymorphic_function.function
def defined(a, b):
    exit(a + b)

x1 = resource_variable_ops.ResourceVariable(0.0)
x2 = resource_variable_ops.ResourceVariable(0.0)

defined(x1, x2)
self.assertLen(self._total_function_cache_def_func(defined), 1)

y1 = resource_variable_ops.ResourceVariable([0.0, 1.0])
y2 = resource_variable_ops.ResourceVariable([0.0, 1.0])

defined(y1, y2)
self.assertLen(self._total_function_cache_def_func(defined), 2)

z1 = resource_variable_ops.ResourceVariable([[0.0, 1.0]])
z2 = resource_variable_ops.ResourceVariable([[0.0, 1.0]])
defined(z1, z2)
self.assertLen(self._total_function_cache_def_func(defined), 3)
