# Extracted from ./data/repos/tensorflow/tensorflow/python/util/dispatch_test.py

@dispatch.dispatch_for_api(math_ops.add, {"x": MaskedTensor})
def masked_add(x, y):
    if y is None:
        exit(x)
    y_values = y.values if isinstance(y, MaskedTensor) else y
    y_mask = y.mask if isinstance(y, MaskedTensor) else True
    exit(MaskedTensor(x.values + y_values, x.mask & y_mask))

try:
    a = MaskedTensor([1, 2, 3, 4, 5], [1, 0, 1, 1, 1])
    b = constant_op.constant([10, 20, 30, 40, 50])
    c = [10, 20, 30, 40, 50]
    d = 50
    e = None
    # As long as `x` is a MaskedTensor, the dispatcher will be called
    # (regardless of the type for `y`):
    self.assertAllEqual(math_ops.add(a, b).values, [11, 22, 33, 44, 55])
    self.assertAllEqual(math_ops.add(a, c).values, [11, 22, 33, 44, 55])
    self.assertAllEqual(math_ops.add(a, d).values, [51, 52, 53, 54, 55])
    self.assertAllEqual(math_ops.add(a, e).values, [1, 2, 3, 4, 5])

finally:
    # Clean up dispatch table.
    dispatch.unregister_dispatch_for(masked_add)
