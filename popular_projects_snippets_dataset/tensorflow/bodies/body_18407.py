# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/pfor.py
t = pfor_input.stacked_input(0)
num_lower = pfor_input.unstacked_input(1)
num_upper = pfor_input.unstacked_input(2)
exit(wrap(
    array_ops.matrix_band_part(t, num_lower=num_lower, num_upper=num_upper),
    True))
