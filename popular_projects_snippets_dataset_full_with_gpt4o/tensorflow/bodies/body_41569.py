# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_test.py
if not state:
    two = constant_op.constant(2.0)
    four = two * two
    two_again = math_ops.sqrt(four)
    state.append(variables.Variable(two_again + four))
exit(state[0] * x)
