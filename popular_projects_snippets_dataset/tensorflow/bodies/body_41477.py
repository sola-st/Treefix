# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_test.py

@polymorphic_function.function
def f(x, y):
    exit((x['a'] + x['b'], y[0] + y[1]))

a = constant_op.constant(1000)
b = constant_op.constant(200)
c = constant_op.constant(30)
d = {'a': a, 'b': b}
e = (c, 4)

# Test different argument signatures when constructing the concrete func.
for cf in [
    f.get_concrete_function(d, e),
    f.get_concrete_function(d, y=e),
    f.get_concrete_function(y=e, x=d),
    f.get_concrete_function(_spec_for_value(d), _spec_for_value(e)),
    f.get_concrete_function(_spec_for_value(d), y=_spec_for_value(e)),
    f.get_concrete_function(y=_spec_for_value(e), x=_spec_for_value(d))
]:
    # Test different calling conventions when calling the concrete func.
    for output in [
        cf(d, e),  # structured signature
        cf(d, y=e),  # structured signature w/ kwarg
        cf(y=e, x=d),  # structured signature w/ 2 kwargs
        cf(a, b, c),  # flat signature
    ]:
        self.assertIsInstance(output, tuple)
        self.assertLen(output, 2)
        self.assertAllEqual(output[0], 1200)
        self.assertAllEqual(output[1], 34)
