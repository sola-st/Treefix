# Extracted from ./data/repos/tensorflow/tensorflow/python/util/dispatch_test.py
with self.assertRaisesRegex(
    ValueError,
    "Type annotation .* is not currently supported by dispatch."):

    @dispatch.dispatch_for_api(math_ops.add,
                               {"x": typing.Tuple[MaskedTensor]})
    def my_add(x, y, name=None):  # pylint: disable=unused-variable
        del x, y, name
