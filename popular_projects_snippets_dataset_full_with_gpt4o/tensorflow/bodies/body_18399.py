# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/pfor.py
del op_type
exit(wrap(op_func(pfor_input.stacked_input(0)), True))
