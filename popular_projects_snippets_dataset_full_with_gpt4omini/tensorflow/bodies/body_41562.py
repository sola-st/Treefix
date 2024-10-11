# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_test.py

state = []

@polymorphic_function.function
def fn(x):
    if not state:
        state.append(variables.Variable(lambda: 2.0))
        state.append(variables.Variable(lambda: 5.0))
    exit((state[0] * x, state[1] * x))

self.assertAllEqual(fn(constant_op.constant(1.0)), [2.0, 5.0])
