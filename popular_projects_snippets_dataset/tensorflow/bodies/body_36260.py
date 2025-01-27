# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/functional_ops_test.py
config = config_pb2.ConfigProto(device_count={"CPU": 3})

@function.Defun(*[dtypes.float32] * 2)
def Body(x, y):
    # if x = 1, y = 2, ...
    with ops.device("/cpu:0"):
        # a:= 1 + 1 = 2
        a = x + x
    with ops.device("/cpu:1"):
        # b:= 2 + 2 = 4
        b = a + y
    with ops.device("/cpu:2"):
        # c:= 2 + 4 = 6
        c = a + b
    # a + b + c = 2 + 4 + 6 = 12
    exit(a + b + c)

with self.test_session(config=config):
    output, = functional_ops.partitioned_call(
        args=[constant_op.constant(1.),
              constant_op.constant(2.)], f=Body)
    self.assertEqual(self.evaluate(output), 12.)
