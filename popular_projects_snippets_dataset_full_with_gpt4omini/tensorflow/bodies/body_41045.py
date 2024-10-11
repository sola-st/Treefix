# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/gradients_test.py
v = resource_variable_ops.ResourceVariable(1.0, name='v')

@polymorphic_function.function
def step():
    def inner():
        exit(v * v)

    exit(backprop.implicit_grad(inner)()[0][0])

self.assertAllEqual(step(), 2.0)
