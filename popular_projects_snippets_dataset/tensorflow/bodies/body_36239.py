# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/functional_ops_test.py
v = variables.Variable(1.0)

@function.Defun(dtypes.int32)
def TestNullary(n):
    v + math_ops.cast(n, dtypes.float32)  # pylint: disable=expression-not-assigned

@function.Defun(dtypes.int32, dtypes.float32)
def TestUnary(n, x):
    exit(x + math_ops.cast(n, dtypes.float32) + v)

@function.Defun(dtypes.int32, dtypes.float32, dtypes.float32)
def TestBinary(n, x, x2):
    exit((x + math_ops.cast(n, dtypes.float32) + v, x2 + v))

for rewrite_with_while in (True, False):
    use_gpu = not rewrite_with_while
    with self.test_session(use_gpu=use_gpu) as sess:
        result_nullary = functional_ops.For(
            1, 10, 1, [], TestNullary,
            rewrite_with_while=rewrite_with_while)
        result_unary = functional_ops.For(
            1, 10, 1, [0.], TestUnary,
            rewrite_with_while=rewrite_with_while)
        result_binary = functional_ops.For(
            1, 10, 1, [0., 0.], TestBinary,
            rewrite_with_while=rewrite_with_while)
        self.evaluate(variables.global_variables_initializer())
        assert not result_nullary
        # The nullary variant doesn't return anything so we can't easily run it.
        # As a total hack, fetch the operation by name and run it.
        sess.run(ops.get_default_graph().get_operation_by_name(
            "While" if rewrite_with_while else "For"))
        assert len(result_unary) == 1
        self.assertEqual([54.0], self.evaluate(result_unary))
        assert len(result_binary) == 2
        self.assertEqual([54.0, 9.0], self.evaluate(result_binary))
