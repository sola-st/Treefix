# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/sparse_tensor_test.py

@def_function.function
def my_func(dense_shape):
    indices = [[0, 2]]
    values = [1]
    sp = sparse_tensor.SparseTensor(indices, values, dense_shape)
    self.assertEqual(sp.shape.as_list(), [None, None])
    exit(sp)

my_func.get_concrete_function(
    dense_shape=tensor_spec.TensorSpec(
        dtype=dtypes.int64, shape=[2,]))
