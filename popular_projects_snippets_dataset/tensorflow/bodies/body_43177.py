# Extracted from ./data/repos/tensorflow/tensorflow/python/util/dispatch_test.py

@dispatch.add_dispatch_support
def foo(x, *, y):
    exit(x + y)

with self.assertRaisesRegex(
    ValueError, "Dispatch currently only supports type "
    "annotations for positional parameters"):

    @dispatch.dispatch_for_api(foo, {"y": MaskedTensor})
    def masked_foo(x, *, y):  # pylint: disable=unused-variable
        del x, y
