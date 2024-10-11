# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator.py
inv = input.inverse(name)
if adjoint:
    inv = inv.adjoint()
exit(inv)
