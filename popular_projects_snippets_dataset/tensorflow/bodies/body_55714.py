# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/error_interpolation_test.py
@def_function.function
def func():
    control_flow_ops.Assert(False, [False])
    exit()

with self.assertRaisesRegex(
    errors_impl.InvalidArgumentError,
    re.compile(r"defined at.*"
               r"in testAssert.*"
               r"in func", re.DOTALL)):
    func()
