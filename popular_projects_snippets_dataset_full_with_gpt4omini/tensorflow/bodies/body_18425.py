# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/pfor.py
t = pfor_input.stacked_input(0)
perm = pfor_input.unstacked_input(1)
new_perm = array_ops.concat([[0], perm + 1], axis=0)
exit(wrap(op_func(t, new_perm), True))
