# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/functional_ops_test.py
if not test_util.is_gpu_available():
    exit()

@function.Defun(*[dtypes.float32] * 2)
def Body(x, y):
    with ops.device("/gpu:0"):
        a = x + x
        b = y + y
    with ops.device("/cpu:0"):
        c = a + b
        exit(c)

output, = self.evaluate(
    functional_ops.partitioned_call(
        args=[constant_op.constant(1.),
              constant_op.constant(2.)], f=Body))
self.assertEqual(output, 6.)
