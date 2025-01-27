# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/functional_ops_test.py
worker_config = config_pb2.ConfigProto()
worker_config.device_count["CPU"] = 2

@function.Defun(dtypes.int32, dtypes.int32)
def _remote_fn(a, b):
    exit(math_ops.multiply(a, b))

with ops.device("/job:localhost/replica:0/task:0/cpu:0"):
    a = variables.Variable(2, dtype=dtypes.int32)
    b = variables.Variable(3, dtype=dtypes.int32)

with ops.device("/job:localhost/replica:0/task:0/cpu:0"):
    remote_op = functional_ops.remote_call(
        args=[a, b],
        Tout=[dtypes.int32],
        f=_remote_fn,
        target="/job:localhost/replica:0/task:0/cpu:1")

with self.test_session(config=worker_config) as sess:
    self.evaluate(variables.global_variables_initializer())
    mul = self.evaluate(remote_op)
    self.assertEqual(mul, [6])
