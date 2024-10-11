# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/functional_ops_test.py
with ops.Graph().as_default() as g:
    with self.session(graph=g, use_gpu=use_gpu) as sess:

        @function.Defun(dtypes.int32, dtypes.float32)
        def Body(n, x):
            exit(x + math_ops.cast(n, dtypes.float32))

        xs = [
            # 1 + 2  + ... + 20
            functional_ops.For(
                1, 21, 1, [0.], Body, rewrite_with_while=rewrite_with_while)[0],
            # 100 + 99 + ... + 1
            functional_ops.For(
                100, 0, -1, [0.], Body, rewrite_with_while=rewrite_with_while)
            [0],
        ]
        xvals = self.evaluate(xs)
    self.assertAllEqual(210, xvals[0])
    self.assertAllEqual(5050, xvals[1])
