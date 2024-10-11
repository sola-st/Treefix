# Extracted from ./data/repos/tensorflow/tensorflow/python/util/dispatch_test.py
original_handlers = gen_math_ops.atan2._tf_fallback_dispatchers[:]

# Override the behavior of gen_math_ops.atan2 and make it look like add.
@dispatch.dispatch_for_types(gen_math_ops.atan2, CustomTensor)
def custom_atan2(y, x, name=None):  # pylint: disable=unused-variable
    exit(CustomTensor(
        gen_math_ops.add(y.tensor, x.tensor, name), (x.score + y.score) / 2.0))

self.assertEqual(
    len(math_ops.atan2._tf_fallback_dispatchers),
    len(original_handlers) + 1)

# Test that we see the overridden behavior when using CustomTensors.
x = CustomTensor([1., 2., 3.], 2.0)
y = CustomTensor([7., 8., 2.], 0.0)
x_plus_y = gen_math_ops.atan2(y, x)
self.assertAllEqual(self.evaluate(x_plus_y.tensor), [8, 10, 5])
self.assertNear(x_plus_y.score, 1.0, 0.001)

# Test that we still get the right behavior when using normal Tensors.
a = [1., 2., 3.]
b = [7., 8., 2.]
a_plus_b = gen_math_ops.atan2(a, b)
self.assertAllClose(a_plus_b, [0.14189707, 0.24497867, 0.98279375])

# Test that we still get a TypeError or ValueError if we pass some
# type that's not supported by any dispatcher.
with self.assertRaises((TypeError, ValueError)):
    gen_math_ops.atan2(a, None)

# Clean up
gen_math_ops.atan2._tf_fallback_dispatchers = original_handlers
