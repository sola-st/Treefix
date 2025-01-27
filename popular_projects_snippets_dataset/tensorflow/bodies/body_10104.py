# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/math_ops_test.py
tensor = array_ops.ones([10, 10])
result = math_ops.scalar_mul(3, tensor)
expected = array_ops.ones([10, 10]) * 3

with test_util.device(use_gpu=True):
    self.assertAllEqual(self.evaluate(expected), self.evaluate(result))
