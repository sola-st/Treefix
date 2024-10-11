# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/math_ops_test.py
const = constant_op.constant(10)
result = math_ops.scalar_mul(3, const)
with test_util.device(use_gpu=True):
    self.assertEqual(30, self.evaluate(result))
