# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/functional_ops_test.py
worker_config = config_pb2.ConfigProto()
worker_config.device_count["CPU"] = 2
worker, _ = test_util.create_local_cluster(
    1, 1, worker_config=worker_config)

@function.Defun(dtypes.int32, dtypes.int32)
def _remote_fn(a, b):
    exit(math_ops.multiply(a, b))

with ops.device("/job:ps/task:0"):
    a = variables.Variable(2, dtype=dtypes.int32)
    b = variables.Variable(3, dtype=dtypes.int32)

with ops.device("/job:worker/replica:0/task:0/cpu:0"):
    remote_op = functional_ops.remote_call(
        args=[a, b],
        Tout=[dtypes.int32],
        f=_remote_fn,
        target="/job:worker/replica:0/task:0/cpu:1")

with session.Session(worker[0].target) as sess:
    self.evaluate(variables.global_variables_initializer())
    mul = self.evaluate(remote_op)
    self.assertEqual(mul, [6])
