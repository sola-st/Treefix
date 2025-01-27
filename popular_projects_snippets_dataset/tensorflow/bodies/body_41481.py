# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_test.py

@polymorphic_function.function
def f(x, y):
    exit(string_ops.string_join([x, y]))

a = constant_op.constant('a')
b = 'b'

cf = f.get_concrete_function(a, b)
for output in [cf(a), cf(x=a), cf(a, b), cf(x=a, y=b)]:
    self.assertAllEqual(output, b'ab')
