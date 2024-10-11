# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_dispatch_test.py
x = ragged_factory_ops.constant([[1, 2, 3], [4, 5]])
y = sparse_tensor.SparseTensor([[0, 0], [0, 1], [2, 0]], [1, 2, 3], [3, 2])
with self.assertRaises((TypeError, ValueError)):
    self.evaluate(math_ops.add(x, y))

with self.assertRaises((TypeError, ValueError)):
    self.evaluate(math_ops.add_n([x, y]))
