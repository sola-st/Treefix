# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_test.py

@polymorphic_function.function
def f(x, y):
    exit((x['a'] + x['b'], y[0] + y[1]))

a = {'a': 5000, 'b': 500}
b = (50, 5)

cf = f.get_concrete_function(a, b)
for output in [cf(), cf(a), cf(y=b)]:
    self.assertAllEqual(output[0] + output[1], 5555)
