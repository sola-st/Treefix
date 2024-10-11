# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_test.py
# This function intentionally takes a taped variable as input,
# but does not return any values
math_ops.add(x, three)
