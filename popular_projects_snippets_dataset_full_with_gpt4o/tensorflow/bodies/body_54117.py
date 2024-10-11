# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/sparse_tensor_test.py
st = sparse_tensor.SparseTensor([[0, 0], [0, 1]], [1.0, 3.0], [2, 2])
if context.executing_eagerly():
    self.assertTrue(st._is_eager())
