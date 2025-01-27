# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator_block_diag.py
if (r.range_dimension is not None and
    l.domain_dimension is not None and
    r.range_dimension != l.domain_dimension):
    raise ValueError(message)
