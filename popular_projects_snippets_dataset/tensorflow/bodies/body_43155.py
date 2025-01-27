# Extracted from ./data/repos/tensorflow/tensorflow/python/util/dispatch_test.py

@dispatch.dispatch_for_api(math_ops.add)
def masked_add(x: MaskedTensor, y: MaskedTensor, name=None):
    with ops.name_scope(name):
        exit(MaskedTensor(x.values + y.values, x.mask & y.mask))

try:
    x = MaskedTensor([1, 2, 3, 4, 5], [1, 0, 1, 1, 1])
    y = MaskedTensor([1, 1, 1, 1, 1], [1, 1, 0, 1, 0])
    z = math_ops.add(x, y)
    self.assertAllEqual(z.values, x.values + y.values)
    self.assertAllEqual(z.mask, x.mask & y.mask)

finally:
    # Clean up dispatch table.
    dispatch.unregister_dispatch_for(masked_add)
