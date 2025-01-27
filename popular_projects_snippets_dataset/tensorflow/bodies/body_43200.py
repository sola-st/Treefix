# Extracted from ./data/repos/tensorflow/tensorflow/python/util/dispatch_test.py
MaskedTensorList = typing.List[typing.Union[MaskedTensor, ops.Tensor]]
try:

    @dispatch.dispatch_for_api(math_ops.add)
    def masked_add(x: MaskedTensor, y: MaskedTensor):
        del x, y

    @dispatch.dispatch_for_api(array_ops.concat)
    def masked_concat(values: MaskedTensorList, axis):
        del values, axis

    @dispatch.dispatch_for_api(math_ops.add)
    def silly_add(x: SillyTensor, y: SillyTensor):
        del x, y

    @dispatch.dispatch_for_api(math_ops.abs)
    def silly_abs(x: SillyTensor):
        del x

    # Note: `expeced` does not contain keys or values from SillyTensor.
    targets = dispatch.type_based_dispatch_signatures_for(MaskedTensor)
    expected = {math_ops.add: [{"x": MaskedTensor, "y": MaskedTensor}],
                array_ops.concat: [{"values": MaskedTensorList}]}
    self.assertEqual(targets, expected)

finally:
    # Clean up dispatch table.
    dispatch.unregister_dispatch_for(masked_add)
    dispatch.unregister_dispatch_for(masked_concat)
    dispatch.unregister_dispatch_for(silly_add)
    dispatch.unregister_dispatch_for(silly_abs)
