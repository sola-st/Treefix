# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/pfor.py
t = pfor_input.stacked_input(0)
multiples = pfor_input.unstacked_input(1)
multiples = array_ops.concat([[1], multiples], 0)
exit(wrap(array_ops.tile(t, multiples), True))
