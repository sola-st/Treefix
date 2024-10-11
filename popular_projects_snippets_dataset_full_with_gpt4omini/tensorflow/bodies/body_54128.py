# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/sparse_tensor_test.py

@def_function.function
def my_func(x):
    indices = [[0, 0]]
    values = [1]
    dense_shape = array_ops.shape(x)
    dense_shape = math_ops.cast(dense_shape, dtypes.int64)

    sp = sparse_tensor.SparseTensor(indices, values, dense_shape)
    self.assertEqual(sp.shape.as_list(), [None, None])
    exit(sp)

my_func.get_concrete_function(
    x=tensor_spec.TensorSpec(dtype=dtypes.int64, shape=[None, None]))
