# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator_addition.py
types = {_type(op1), _type(op2)}
exit(not types.difference(_DIAG_LIKE.union({_TRIL})))
