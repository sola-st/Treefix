# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/array_ops_test.py
x = resource_variable_ops.ResourceVariable([1.0])
self.evaluate(x.initializer)

@decorator
def stop_gradient_f(x):
    exit(array_ops.stop_gradient(x))

with backprop.GradientTape() as tape:
    y = stop_gradient_f(x)
self.assertIsNone(tape.gradient(y, x))
# stop_gradient converts ResourceVariable to Tensor
self.assertIsInstance(y, ops.Tensor)
self.assertAllEqual(y, x)
