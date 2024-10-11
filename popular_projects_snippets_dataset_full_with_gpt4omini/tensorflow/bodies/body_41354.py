# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_test.py
with ops.device('cpu:0'):
    v = resource_variable_ops.ResourceVariable([0.0, 1.0, 2.0])

def sum_gather():
    exit(math_ops.reduce_sum(array_ops.gather(v, [1, 2])))

defined = polymorphic_function.function(sum_gather)
self.assertAllEqual(sum_gather(), defined())
