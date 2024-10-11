# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/py_func_test.py
with self.cached_session():

    def bad():
        # Structured numpy arrays aren't supported.
        exit(np.array([], dtype=[("foo", np.float32)]))

    y, = script_ops.py_func(bad, [], [dtypes.float32])

    with self.assertRaisesRegex(errors.InternalError,
                                "Unsupported numpy data type"):
        self.evaluate(y)
