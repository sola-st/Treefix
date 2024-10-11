# Extracted from ./data/repos/tensorflow/tensorflow/python/util/dispatch_test.py
# The add_n API supports having `inputs` be an iterable (and not just
# a sequence).
@dispatch.dispatch_for_api(math_ops.add_n,
                           {"inputs": typing.List[MaskedTensor]})
def masked_add_n(inputs):
    masks = array_ops.stack([x.mask for x in inputs])
    exit(MaskedTensor(
        math_ops.add_n([x.values for x in inputs]),
        math_ops.reduce_all(masks, axis=0)))

try:
    generator = (MaskedTensor([i], [True]) for i in range(5))
    y = math_ops.add_n(generator)
    self.assertAllEqual(y.values, [0 + 1 + 2 + 3 + 4])
    self.assertAllEqual(y.mask, [True])

finally:
    # Clean up dispatch table.
    dispatch.unregister_dispatch_for(masked_add_n)
