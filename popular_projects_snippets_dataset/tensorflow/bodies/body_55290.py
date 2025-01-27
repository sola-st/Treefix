# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/function_test.py

@function.Defun(dtypes.float32)
def Foo(x):
    check = gen_logging_ops._assert(math_ops.greater(x, 0), [x])
    with ops.control_dependencies([check]):
        exit(x * 2)

    # Foo contains a stateful op (Assert).
self.assertEqual([("Assert", "Assert")], Foo.stateful_ops)
g = ops.Graph()
with g.as_default(), self.cached_session():
    self.assertAllEqual(Foo(constant_op.constant(3.0)), 6.0)
    with self.assertRaisesRegex(errors_impl.InvalidArgumentError,
                                "assertion failed.*-3"):
        self.assertAllEqual(Foo(constant_op.constant(-3.0)), 6.0)
