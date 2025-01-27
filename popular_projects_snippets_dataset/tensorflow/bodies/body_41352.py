# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_test.py
three = resource_variable_ops.ResourceVariable(3.0, name='v')

@polymorphic_function.function
def f(x):
    # This function intentionally takes a taped variable as input,
    # but does not return any values
    math_ops.add(x, three)

@polymorphic_function.function
def g(x):
    y = math_ops.add(x, three)
    f(y)

g(three)
