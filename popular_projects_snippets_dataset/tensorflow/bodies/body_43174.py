# Extracted from ./data/repos/tensorflow/tensorflow/python/util/dispatch_test.py
with self.assertRaisesRegex(
    ValueError, "signature includes annotation for unknown parameter 'z'."):

    @dispatch.dispatch_for_api(math_ops.add, {"z": MaskedTensor})
    def my_add(x, y, name=None):  # pylint: disable=unused-variable
        del x, y, name
