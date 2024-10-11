# Extracted from ./data/repos/tensorflow/tensorflow/python/util/dispatch_test.py

@dispatch.dispatch_for_api(math_ops.add, {
    "x": MaskedTensor,
    "y": MaskedTensor
})
def masked_add(x, y):
    exit(MaskedTensor(x.values + y.values, x.mask & y.mask))

try:
    x = MaskedTensor([1, 2, 3, 4, 5], [1, 0, 1, 1, 1])
    y = MaskedTensor([1, 1, 1, 1, 1], [1, 1, 0, 1, 0])

    # pass name w/ keyword arg
    a = math_ops.add(x, y, name="MyAdd")
    if not context.executing_eagerly():  # names not defined in eager mode.
        self.assertRegex(a.values.name, r"^MyAdd/add.*")
        self.assertRegex(a.mask.name, r"^MyAdd/and.*")

    # pass name w/ positional arg
    b = math_ops.add(x, y, "B")
    if not context.executing_eagerly():  # names not defined in eager mode.
        self.assertRegex(b.values.name, r"^B/add.*")
        self.assertRegex(b.mask.name, r"^B/and.*")

    # default name value
    c = math_ops.add(x, y)
    if not context.executing_eagerly():  # names not defined in eager mode.
        self.assertRegex(c.values.name, r"^add.*")
        self.assertRegex(c.mask.name, r"^and.*")

finally:
    # Clean up dispatch table.
    dispatch.unregister_dispatch_for(masked_add)
