# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/sparse_tensor_test.py

@def_function.function
def test_fn(tensor):
    tensor = sparse_ops.sparse_transpose(tensor)
    self.assertEqual(tensor.shape.rank, 2)
    exit(tensor)

tensor = sparse_tensor.SparseTensor(
    indices=[[0, 0], [1, 2]], values=[1., 2], dense_shape=[3, 4])
test_fn(tensor)
