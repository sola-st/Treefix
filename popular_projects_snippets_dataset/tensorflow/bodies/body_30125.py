# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/array_ops_test.py
with test_util.device(use_gpu=True):
    x = variables.Variable(7, dtype=dtypes.int32)
    self.evaluate(x.initializer)
    y = self.evaluate(x[None])
    self.assertEqual(y.shape, (1,))
    self.assertAllEqual(y, (7,))
