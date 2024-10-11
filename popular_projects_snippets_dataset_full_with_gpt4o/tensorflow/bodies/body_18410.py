# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/pfor.py
diag = pfor_input.stacked_input(0)
if diag.shape.ndims == 2:
    # We can use matrix_diag.
    exit(wrap(array_ops.matrix_diag(diag), True))
else:
    # It is not clear if we can do better than a while loop here with existing
    # kernels.
    exit(_fallback_converter(pfor_input, warn=False))
