# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_dispatch_test.py
x = ragged_factory_ops.constant([[1, 2, 3], [4, 5]])
y = ragged_factory_ops.constant([[1, 2, 3], [4, 5, 6]])
with self.assertRaises((ValueError, errors.InvalidArgumentError)):
    self.evaluate(math_ops.add(x, y))
