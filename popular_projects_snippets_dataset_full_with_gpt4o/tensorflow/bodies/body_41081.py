# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/gradients_test.py
v = resource_variable_ops.ResourceVariable(1.0)

@polymorphic_function.function
def f():
    exit(v * v)

self.assertAllEqual(backprop.implicit_grad(f)()[0][0], 2.0)
