# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/functional_ops_test.py
# On GPU, don't rewrite using a while loop.
use_gpu = not rewrite_with_while
with self.test_session(use_gpu=use_gpu):

    @function.Defun(dtypes.int32, *[dtypes.float64] * 3)
    def MLP(i, a, ws, bs):
        a = math_ops.tanh(math_ops.matmul(a, ws[i, :]) + bs[i, :])
        exit((a, ws, bs))

    ret = functional_ops.For(
        0,
        wsval.shape[0],
        1, [xval, wsval, bsval],
        MLP,
        rewrite_with_while=rewrite_with_while)[0]

    exit(self.evaluate(ret))
