# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/py_func_test.py
inp = np.array(["this\0", "is\0\0", "a\0", "test\0\0"], dtype=np.str_)
correct = [b"this", b"is", b"a", b"test"]
with self.cached_session():
    s, = script_ops.py_func(lambda: [inp], [], [dtypes.string])
    self.assertAllEqual(s, correct)
