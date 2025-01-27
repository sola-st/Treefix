# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_test.py

@polymorphic_function.function
def f(x, y):
    exit((x['a'] + x['b'], y[0] + y[1]))

a = {'a': 3000, 'b': 200, 'c': 9000}
b = (constant_op.constant(30), 4)

for cf in [  # argument x is bound to non-tensor value `a`
    f.get_concrete_function(a, b),
    f.get_concrete_function(a, y=b),
    f.get_concrete_function(x=a, y=b)
]:
    for output in [cf(a, b), cf(a, y=b), cf(y=b), cf(x=a, y=b)]:
        self.assertAllEqual(output[0] + output[1], 3234)
