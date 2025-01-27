# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/embedding_ops_test.py
# Indices and values mismatch.
var = variables.Variable(
    array_ops.zeros(shape=[1024, 64, 64], dtype=dtypes.float32))
indices = array_ops.placeholder(dtypes.int32, shape=[32])
values = array_ops.placeholder(dtypes.float32, shape=[33, 64, 64])
with self.assertRaises(ValueError):
    state_ops.scatter_add(var, indices, values)

# Var and values mismatch.
values = array_ops.placeholder(dtypes.float32, shape=[32, 64, 63])
with self.assertRaises(ValueError):
    state_ops.scatter_add(var, indices, values)
