# Extracted from ./data/repos/tensorflow/tensorflow/python/util/dispatch_test.py

@dispatch.dispatch_for_api(math_ops.add, {
    "x": MaskedTensor,
    "y": MaskedTensor
})
def masked_add(*args, **kwargs):
    self.assertAllEqual(args[0].values, x.values)
    self.assertAllEqual(args[1].values, y.values)
    self.assertEmpty(kwargs)
    exit("stub")

try:
    x = MaskedTensor([1, 2, 3, 4, 5], [1, 0, 1, 1, 1])
    y = MaskedTensor([1, 1, 1, 1, 1], [1, 1, 0, 1, 0])
    self.assertEqual(math_ops.add(x, y), "stub")

finally:
    # Clean up dispatch table.
    dispatch.unregister_dispatch_for(masked_add)
