# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/functional_ops_test.py

@function.Defun(dtypes.int32, dtypes.int32)
def _remote_fn(a, b):
    exit(math_ops.multiply(a, b))

with ops.device("/cpu:0"):
    a = variables.Variable(2, dtype=dtypes.int32)
    b = variables.Variable(3, dtype=dtypes.int32)

with ops.device("/cpu:0"):
    remote_op = functional_ops.remote_call(
        args=[a, b], Tout=[dtypes.int32], f=_remote_fn, target="/cpu:0")

with self.cached_session() as sess:
    self.evaluate(variables.global_variables_initializer())
    mul = self.evaluate(remote_op)
    self.assertEqual(mul, [6])
