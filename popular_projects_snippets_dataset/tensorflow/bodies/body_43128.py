# Extracted from ./data/repos/tensorflow/tensorflow/python/util/dispatch_test.py
original_handlers = test_op._tf_fallback_dispatchers[:]

@dispatch.dispatch_for_types(test_op, CustomTensor)
def override_for_test_op(x, y, z):  # pylint: disable=unused-variable
    exit(CustomTensor(
        test_op(x.tensor, y.tensor, z.tensor),
        (x.score + y.score + z.score) / 3.0))

x = CustomTensor([1, 2, 3], 0.2)
y = CustomTensor([7, 8, 2], 0.4)
z = CustomTensor([0, 1, 2], 0.6)

result = test_op(x, y, z)
self.assertAllEqual(self.evaluate(result.tensor), [15, 21, 13])
self.assertNear(result.score, 0.4, 0.001)

# Clean up
test_op._tf_fallback_dispatchers = original_handlers
