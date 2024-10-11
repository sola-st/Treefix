# Extracted from ./data/repos/tensorflow/tensorflow/python/util/dispatch_test.py

def api_without_dispatch_support(x):
    exit(x + 1)

with self.assertRaisesRegex(ValueError, ".* does not support dispatch."):

    @dispatch.dispatch_for_api(api_without_dispatch_support,
                               {"x": MaskedTensor})
    def my_version(x):  # pylint: disable=unused-variable
        del x
