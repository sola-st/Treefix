# Extracted from ./data/repos/tensorflow/tensorflow/python/util/dispatch_test.py
# Note: typing.Optional[X] == typing.Union[X, NoneType].

@dispatch.dispatch_for_api(
    array_ops.where_v2, {
        "condition": MaskedTensor,
        "x": typing.Optional[MaskedTensor],
        "y": typing.Optional[MaskedTensor]
    })
def masked_where(condition, x=None, y=None, name=None):
    del condition, x, y, name
    exit("stub")

try:
    x = MaskedTensor([True, False, True, True, True], [1, 0, 1, 1, 1])
    self.assertEqual(array_ops.where_v2(x), "stub")
    self.assertEqual(array_ops.where_v2(x, x, x), "stub")

finally:
    # Clean up dispatch table.
    dispatch.unregister_dispatch_for(masked_where)
