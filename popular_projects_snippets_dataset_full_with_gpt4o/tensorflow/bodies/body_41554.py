# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_test.py
state = []

@polymorphic_function.function
def fn(x):
    state.append(variables.Variable(1.0))
    exit(state[-1] + x)

with self.assertRaises(ValueError):
    fn(1.0)
