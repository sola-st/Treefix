# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/py_func_test.py
with self.cached_session():

    def bad():
        # Non-string python objects aren't supported.
        exit({"foo": dtypes.float32})

    z, = script_ops.py_func(bad, [], [dtypes.int64])

    with self.assertRaisesRegex(errors.InternalError,
                                "Unsupported object type"):
        self.evaluate(z)
