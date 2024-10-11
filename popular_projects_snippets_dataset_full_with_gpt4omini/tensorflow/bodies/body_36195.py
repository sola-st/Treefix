# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/functional_ops_test.py
if not test_util.is_gpu_available():
    self.skipTest("No GPU available")

@function.Defun(dtypes.string)
def _remote_fn(inp):
    exit(array_ops.identity(inp))

a = array_ops.constant("a")

with ops.device("/gpu:0"):
    remote_op = functional_ops.remote_call(
        args=[a], Tout=[dtypes.string], f=_remote_fn, target="/cpu:0")

with self.cached_session() as sess:
    ret = self.evaluate(remote_op)
    self.assertAllEqual(ret, [b"a"])
