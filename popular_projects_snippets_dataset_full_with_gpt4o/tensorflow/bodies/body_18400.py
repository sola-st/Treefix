# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/pfor.py
del op_type
exit(wrap(op_func(*[x.t for x in pfor_input.inputs]), True))
