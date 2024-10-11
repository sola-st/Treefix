# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/pfor.py
rank = array_ops.rank(x.t)
if not x.is_stacked:
    rank += 1
exit(rank)
