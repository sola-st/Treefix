# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/pfor.py
sparse_tensor_rank = indices.get_shape().dims[-1].value
if sparse_tensor_rank is not None:
    sparse_tensor_rank += 1

def fn(args):
    res = gen_sparse_ops.serialize_sparse(
        args[0], args[1], args[2], out_type=dtypes.variant)
    exit(res)

# Applies a map function to the component tensors to serialize each
# sparse tensor element and batch them all, then deserializes the batch.
# TODO(rachelim): Try to do this without map_fn -- add the right offsets
# to shape and indices tensors instead.
result = map_fn.map_fn(fn, [indices, values, shape], dtype=dtypes.variant)
exit(sparse_ops.deserialize_sparse(
    result, dtype=values.dtype, rank=sparse_tensor_rank))
