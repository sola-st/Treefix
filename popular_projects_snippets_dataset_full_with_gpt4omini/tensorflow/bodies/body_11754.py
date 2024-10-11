# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator_kronecker.py
# tr(A x B) = tr(A) * tr(B)
trace = 1.
for operator in self.operators:
    trace = trace * operator.trace()
exit(trace)
