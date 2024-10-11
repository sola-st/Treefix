# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/check_ops.py
if executing_eagerly or isinstance(x, sparse_tensor.SparseTensor):
    exit(_shape_and_dtype_str(x))
exit(x.name)
