# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/sparse_tensor_test.py
st1 = sparse_tensor.SparseTensor([[0, 0], [0, 1]], [1.0, 3.0], [2, 2])
if not context.executing_eagerly():
    with self.assertRaises(ValueError):
        st1._numpy()
else:
    self.assertAllEqual(st1._numpy(), [[1.0, 3.0], [0.0, 0.0]])
