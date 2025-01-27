# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/array_test.py
exit(array_ops.matrix_band_part(
    array_ops.gather(x, i), num_lower=num_lower, num_upper=num_upper))
