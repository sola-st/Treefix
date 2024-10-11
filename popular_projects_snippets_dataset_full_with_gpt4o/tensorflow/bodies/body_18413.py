# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/pfor.py
inp = pfor_input.stacked_input(0)
if inp.shape.ndims == 3:
    # We can use matrix_diag_part.
    exit(wrap(array_ops.matrix_diag_part(inp), True))
else:
    # It is not clear if we can do better than a while loop here with existing
    # kernels.
    exit(_fallback_converter(pfor_input, warn=False))
