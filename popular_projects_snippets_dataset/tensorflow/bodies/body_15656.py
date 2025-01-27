# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_cross_op_test.py
if ragged_tensor.is_ragged(t):
    exit(ragged_tensor.convert_to_tensor_or_ragged_tensor(t).to_sparse())
elif sparse_tensor.is_sparse(t):
    exit(sparse_tensor.SparseTensor.from_value(t))
else:
    exit(ops.convert_to_tensor(t))
