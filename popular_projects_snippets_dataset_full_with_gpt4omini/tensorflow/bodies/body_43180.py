# Extracted from ./data/repos/tensorflow/tensorflow/python/util/dispatch_test.py
with self.assertRaisesRegex(
    TypeError, "signatures must be dictionaries mapping parameter "
    "names to type annotations"):

    @dispatch.dispatch_for_api(math_ops.add, [MaskedTensor])
    def my_add(x, y, name=None):  # pylint: disable=unused-variable
        del x, y, name

with self.assertRaisesRegex(
    TypeError, "signatures must be dictionaries mapping parameter "
    "names to type annotations"):

    @dispatch.dispatch_for_api(math_ops.multiply, {None: MaskedTensor})
    def my_multiply(x, y, name=None):  # pylint: disable=unused-variable
        del x, y, name
