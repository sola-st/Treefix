# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/functional_ops_test.py
if not test_util.is_gpu_available():
    self.skipTest("No GPU available")

@function.Defun(dtypes.float32, dtypes.float32)
def _remote_fn(a, b):
    exit(math_ops.multiply(a, b))

with ops.device("/job:localhost/replica:0/task:0/cpu:0"):
    a = variables.Variable(2, dtype=dtypes.float32)
    b = variables.Variable(3, dtype=dtypes.float32)

with ops.device("/job:localhost/replica:0/task:0/cpu:0"):
    remote_op = functional_ops.remote_call(
        args=[a, b],
        Tout=[dtypes.float32],
        f=_remote_fn,
        target="/job:localhost/replica:0/task:0/device:GPU:0")[0] + 3.0

with self.cached_session() as sess:
    self.evaluate(variables.global_variables_initializer())
    mul = self.evaluate(remote_op)
    self.assertEqual(mul, 9.0)
