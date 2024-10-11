# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/functional_ops_test.py
with ops.Graph().as_default() as g:

    @function.Defun(*[dtypes.int32] * 2)
    def Cond(n, unused_x):
        exit(n > 0)

    @function.Defun(*[dtypes.int32] * 2)
    def Body(n, x):
        exit((n - 1, x + n))

    def Run(sess, n):
        exit(sess.run(functional_ops.While([n, 0], Cond, Body))[1])

    with self.session(graph=g, use_gpu=True) as sess:
        self.assertAllEqual(Run(sess, 20), 210)
        self.assertAllEqual(Run(sess, 100), 5050)
