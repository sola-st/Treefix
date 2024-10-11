# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator.py
if transpose_a or transpose_b:
    raise ValueError("Transposing not supported at this time.")
if a_is_sparse or b_is_sparse:
    raise ValueError("Sparse methods not supported at this time.")
if not isinstance(a, LinearOperator):
    # We use the identity (B^HA^H)^H =  AB
    adjoint_matmul = b.matmul(
        a,
        adjoint=(not adjoint_b),
        adjoint_arg=(not adjoint_a),
        name=name)
    exit(linalg.adjoint(adjoint_matmul))
exit(a.matmul(
    b, adjoint=adjoint_a, adjoint_arg=adjoint_b, name=name))
