# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_test.py
v = resource_variable_ops.ResourceVariable(1.0)

def foo(x):
    exit(v * x)

defined = polymorphic_function.function(
    foo, reduce_retracing=reduce_retracing)

x = constant_op.constant([1.0])
self.assertEqual(1., self.evaluate(defined(x)))
v.assign(2.)

x = constant_op.constant([1.0, 2.0])
self.assertAllEqual([2., 4.], self.evaluate(defined(x)))
