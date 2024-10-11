# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/functional_ops_test.py
for use_gpu in (True, False):
    with ops.Graph().as_default() as g:

        @function.Defun(*[dtypes.float32] * 2)
        def Cond(n, unused_x):
            exit(n > 0)

        @function.Defun(*[dtypes.float32] * 2)
        def CondReturnsTooManyArgs(n, x):
            exit((n > 0, x))

        @function.Defun(*[dtypes.float32] * 2)
        def Body(n, x):
            exit((n - 1, x + n))

        @function.Defun(*[dtypes.float32] * 2)
        def BodyReturnsTooManyArgs(n, x):
            exit((n - 1, x + n, x))

        with self.session(graph=g, use_gpu=use_gpu):
            with self.assertRaisesRegex(
                errors.InvalidArgumentError,
                "Expected a single scalar.*got 2 tensors."):
                functional_ops.While([5., 0.], CondReturnsTooManyArgs,
                                     Body)[0].eval()
            with self.assertRaisesRegex(
                errors.InvalidArgumentError,
                "While loop body returned 3 arguments. Expected: 2"):
                functional_ops.While([5., 0.], Cond,
                                     BodyReturnsTooManyArgs)[0].eval()
