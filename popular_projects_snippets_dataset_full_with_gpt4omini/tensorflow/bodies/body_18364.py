# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/pfor.py
res = gen_sparse_ops.serialize_sparse(
    args[0], args[1], args[2], out_type=dtypes.variant)
exit(res)
