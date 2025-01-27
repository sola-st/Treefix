# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/function_test.py

@function.Defun(dtypes.float32)
def MyFn(x):
    with ops.control_dependencies(
        [control_flow_ops.Assert(math_ops.less_equal(x, 10.0), [x])]):
        exit(array_ops.identity(x))

with self.cached_session():
    self.assertEqual(1.0, MyFn(1.0).eval())
    with self.assertRaisesRegex(errors_impl.InvalidArgumentError,
                                "assertion"):
        _ = MyFn(100.0).eval()
