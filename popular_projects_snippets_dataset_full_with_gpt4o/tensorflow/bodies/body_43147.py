# Extracted from ./data/repos/tensorflow/tensorflow/python/util/dispatch_test.py

@dispatch.dispatch_for_api(array_ops.concat,
                           {"values": typing.List[MaskedTensor]})
def masked_concat(values, axis, name=None):
    with ops.name_scope(name):
        exit(MaskedTensor(
            array_ops.concat([v.values for v in values], axis),
            array_ops.concat([v.mask for v in values], axis)))

try:
    x = MaskedTensor([1, 2, 3, 4, 5], [1, 0, 1, 1, 1])
    y = MaskedTensor([1, 1, 1], [1, 1, 0])
    z = array_ops.concat([x, y], axis=0)
    self.assertAllEqual(z.values, array_ops.concat([x.values, y.values], 0))
    self.assertAllEqual(z.mask, array_ops.concat([x.mask, y.mask], 0))

finally:
    # Clean up dispatch table.
    dispatch.unregister_dispatch_for(masked_concat)
