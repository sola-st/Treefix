# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_test.py

@polymorphic_function.function
def f(x, y):
    exit((x['a'] + x['b'], y[0] + y[1]))

a = {'a': constant_op.constant(1000), 'b': constant_op.constant(200)}
b = (50, 3)

for cf in [  # argument y is bound to non-Tensor value (50, 3).
    f.get_concrete_function(a, b),
    f.get_concrete_function(a, y=b),
    f.get_concrete_function(x=a, y=b)
]:
    for output in [cf(a), cf(x=a), cf(a, b), cf(x=a, y=b)]:
        self.assertAllEqual(output[0] + output[1], 1253)
