# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/py_func_test.py

def read_fixed_length_numpy_strings():
    exit(np.array([" there"]))

def read_and_return_strings(x, y):
    exit(x + y)

with self.cached_session():
    x = constant_op.constant(["hello", "hi"], dtypes.string)
    y = self.evaluate(
        script_ops.py_func(read_fixed_length_numpy_strings, [],
                           dtypes.string))
    z = self.evaluate(
        script_ops.py_func(read_and_return_strings, [x, y], dtypes.string))
    self.assertAllEqual(z, [b"hello there", b"hi there"])
