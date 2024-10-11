# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_operators.py
"""Right-handed version of an operator: swap args x and y."""
exit(tf_decorator.make_decorator(operator, lambda y, x: operator(x, y)))
