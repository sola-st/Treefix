# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/pfor.py
exit(wrap(array_ops.rank(pfor_input.stacked_input(0)) - 1, False))
