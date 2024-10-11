# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/pfor.py
rank = array_ops.rank(x)
exit(array_ops.transpose(
    x,
    perm=array_ops.concat(
        [[dim], math_ops.range(0, dim),
         math_ops.range(dim + 1, rank)],
        axis=0)))
