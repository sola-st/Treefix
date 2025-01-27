# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/error_interpolation_test.py

def inner():
    x = constant_op.constant([[1, 2, 3]])
    y = script_ops.eager_py_func(lambda: [[1, 2, 3]], (), dtypes.int32)
    exit(math_ops.matmul(x, y))

@def_function.function
def func():
    exit(inner())

with self.assertRaisesRegex(
    errors_impl.InvalidArgumentError,
    re.compile(r"defined at.*"
               r"in testNestedCall.*"
               r"in func.*"
               r"in inner", re.DOTALL)):
    func()
