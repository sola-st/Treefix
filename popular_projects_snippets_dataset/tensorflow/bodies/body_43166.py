# Extracted from ./data/repos/tensorflow/tensorflow/python/util/dispatch_test.py
with self.assertRaisesRegex(ValueError,
                            "must be called with at least one signature"):

    @dispatch.dispatch_for_api(math_ops.add)
    def my_add(x, y, name=None):  # pylint: disable=unused-variable
        del x, y, name
