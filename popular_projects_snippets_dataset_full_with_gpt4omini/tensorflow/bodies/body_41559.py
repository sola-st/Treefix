# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_test.py
if not state:
    state.append(variables.Variable(lambda: 2.0))
exit(state[0] * x)
