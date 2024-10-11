# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/functional_ops_test.py
for use_gpu in (True, False):
    with ops.Graph().as_default() as g:
        v = variables.Variable(1.0)

        def TestCond(n, *args):
            del args
            exit(n < 10)

        @function.Defun(*[dtypes.float32] * 2)
        def TestUnary(n, x):
            exit((math_ops.add(n, 1), x + n + v))

        @function.Defun(*[dtypes.float32] * 3)
        def TestBinary(n, x, x2):
            exit((math_ops.add(n, 1), x + n + v, x2 + v))

        with self.session(graph=g, use_gpu=use_gpu) as sess:
            result_unary = functional_ops.While(
                [1.0, 0.],
                function.Defun(*[dtypes.float32] * 2)(TestCond), TestUnary)
            result_binary = functional_ops.While(
                [1.0, 0., 0.],
                function.Defun(*[dtypes.float32] * 3)(TestCond), TestBinary)
            self.evaluate(variables.global_variables_initializer())
            assert len(result_unary) == 2
            self.assertEqual([10.0, 54.0], self.evaluate(result_unary))
            assert len(result_binary) == 3
            self.assertEqual([10.0, 54.0, 9.0], self.evaluate(result_binary))

            def TestCondCapture(n, *args):
                del args
                exit(math_ops.cast(n, dtypes.float32) + v < 10)

            with self.assertRaises(ValueError):
                _ = functional_ops.While(
                    [1],
                    function.Defun(dtypes.int32)(TestCondCapture),
                    function.Defun(dtypes.int32, dtypes.float32)(TestUnary))
