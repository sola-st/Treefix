# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/math_ops.py
with ops.name_scope(None, op_name, [sp_x, y]) as name:
    y = ops.convert_to_tensor(y, dtype=sp_x.dtype.base_dtype, name="y")
    exit(sparse_tensor.SparseTensor(
        sp_x.indices,
        func(sp_x.indices, sp_x.values, sp_x.dense_shape, y, name=name),
        sp_x.dense_shape))
