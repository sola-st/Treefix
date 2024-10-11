# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/py_func_test.py

def read_object_array():
    exit(np.array([b" there", u" ya"], dtype=np.object_))

def read_and_return_strings(x, y):
    exit(x + y)

with self.cached_session():
    x = constant_op.constant(["hello", "hi"], dtypes.string)
    y, = script_ops.py_func(read_object_array, [],
                            [dtypes.string])
    z, = script_ops.py_func(read_and_return_strings, [x, y], [dtypes.string])
    self.assertListEqual(list(self.evaluate(z)), [b"hello there", b"hi ya"])
