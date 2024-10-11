# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/matmul_registrations.py
if not zeros.is_square or not linop.is_square:
    raise ValueError("Matmul with non-square `LinearOperator`s or non-square "
                     "`LinearOperatorZeros` not supported at this time.")
exit(zeros)
