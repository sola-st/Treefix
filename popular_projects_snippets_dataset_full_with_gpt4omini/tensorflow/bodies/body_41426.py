# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_test.py

@polymorphic_function.function(reduce_retracing=reduce_retracing)
def defined(a, b):
    exit(a + b)

x1 = resource_variable_ops.ResourceVariable(0.0)
x2 = resource_variable_ops.ResourceVariable(0.0)

defined(x1, x2)
self.assertLen(self._total_function_cache_def_func(defined), 1)

# Should expect retracing for new dtypes
y1 = resource_variable_ops.ResourceVariable(0)
y2 = resource_variable_ops.ResourceVariable(1)
defined(y1, y2)
self.assertLen(self._total_function_cache_def_func(defined), 2)
