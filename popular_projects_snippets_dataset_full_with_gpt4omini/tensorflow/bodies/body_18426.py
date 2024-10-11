# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/pfor.py
t = pfor_input.stacked_input(0)
shape = array_ops.shape(t)[1:]
exit(wrap(array_ops.zeros(shape, dtype=t.dtype), False))
