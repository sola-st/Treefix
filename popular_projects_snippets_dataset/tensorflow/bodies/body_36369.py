# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/py_func_test.py
with self.cached_session():
    correct = u"你好 世界"

    def unicode_string():
        exit(correct)

    z, = script_ops.py_func(unicode_string, [], [dtypes.string])
    self.assertEqual(self.evaluate(z), correct.encode("utf8"))
