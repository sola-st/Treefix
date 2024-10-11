# Extracted from ./data/repos/tensorflow/tensorflow/python/util/dispatch_test.py
with self.assertRaisesRegex(
    ValueError, r"Dispatch function's signature \(x, why, name=None\) does "
    r"not match API's signature \(x, y, name=None\)."):

    @dispatch.dispatch_for_api(math_ops.add, {"x": MaskedTensor})
    def my_add(x, why, name=None):  # pylint: disable=unused-variable
        del x, why, name
