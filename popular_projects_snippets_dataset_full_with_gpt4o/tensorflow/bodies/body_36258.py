# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/functional_ops_test.py

@function.Defun(*[dtypes.float32] * 2)
def Body(x, y):
    with ops.device("/cpu:0"):
        a = x + x
        b = y + y
        exit(a + b)

output, = self.evaluate(
    functional_ops.partitioned_call(
        args=[constant_op.constant(1.),
              constant_op.constant(2.)], f=Body))
self.assertEqual(output, 6.)
