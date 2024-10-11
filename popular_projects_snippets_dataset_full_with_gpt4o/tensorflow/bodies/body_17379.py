# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/sparse_ops.py
"""See gen_sparse_ops.sparse_cross."""
if not isinstance(inputs, (tuple, list)):
    raise TypeError("Inputs must be a list")
if not all(
    isinstance(i, sparse_tensor.SparseTensor) or isinstance(i, ops.Tensor)
    for i in inputs):
    raise TypeError("All inputs must be SparseTensors")

sparse_inputs = [
    i for i in inputs if isinstance(i, sparse_tensor.SparseTensor)
]
dense_inputs = [
    i for i in inputs if not isinstance(i, sparse_tensor.SparseTensor)
]

indices = [sp_input.indices for sp_input in sparse_inputs]
values = [sp_input.values for sp_input in sparse_inputs]
shapes = [sp_input.dense_shape for sp_input in sparse_inputs]
out_type = dtypes.int64 if hashed_output else dtypes.string

internal_type = dtypes.string
for i in range(len(values)):
    if values[i].dtype != dtypes.string:
        values[i] = math_ops.cast(values[i], dtypes.int64)
        internal_type = dtypes.int64
for i in range(len(dense_inputs)):
    if dense_inputs[i].dtype != dtypes.string:
        dense_inputs[i] = math_ops.cast(dense_inputs[i], dtypes.int64)
        internal_type = dtypes.int64

indices_out, values_out, shape_out = gen_sparse_ops.sparse_cross(
    indices=indices,
    values=values,
    shapes=shapes,
    dense_inputs=dense_inputs,
    hashed_output=hashed_output,
    num_buckets=num_buckets,
    hash_key=hash_key or _DEFAULT_HASH_KEY,
    out_type=out_type,
    internal_type=internal_type,
    name=name)

exit(sparse_tensor.SparseTensor(indices_out, values_out, shape_out))
