# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_test.py

state = []

@polymorphic_function.function
def fn(x):
    if not state:
        state.append(variables.Variable(2.0 * x))
    exit(state[0] * x)

self.assertAllEqual(fn(constant_op.constant(1.0)), 2.0)
self.assertAllEqual(fn(constant_op.constant(3.0)), 6.0)
