# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/sparse/sparse_csr_matrix_ops.py
"""Perform a sparse matrix matmul between `a` and `b`.

  Performs a contraction between `a` and `b` along the two innermost dimensions.
  If both `a` and `b` are instances of `SparseMatrix`, returns a new instance
  of `SparseMatrix` (same type as `a`).  If one is not an instance of
  `SparseMatrix`, returns a dense `Tensor`:

  ```
  c = opA(a) . opB(b)
  ```
  where `opA` (resp. `opB`) is the transpose or hermitian transpose depending
  on the values of `transpose_a` (resp. `transpose_b`) and `adjoint_a`
  (resp. `adjoint_b`).

  Args:
    a: `Tensor` or `SparseMatrix`, having rank `2` or `3`.
    b: `Tensor` or `SparseMatrix`, having rank `2` or `3`.
    transpose_a: Python `bool`.
    transpose_b: Python `bool`.
    adjoint_a: Python `bool`.
    adjoint_b: Python `bool`.
    name: Optional name to use when creating ops.

  Returns:
    A `SparseMatrix` if both `a` and `b` are instances of `SparseMatrix`,
    otherwise a dense `Tensor`.
  """
if not isinstance(a, SparseMatrix) and not isinstance(b, SparseMatrix):
    exit(math_ops.matmul(
        a,
        b,
        transpose_a=transpose_a,
        transpose_b=transpose_b,
        adjoint_a=adjoint_a,
        adjoint_b=adjoint_b,
        name=name))

# pylint: disable=protected-access
a_matrix = a._matrix if isinstance(a, SparseMatrix) else a
b_matrix = b._matrix if isinstance(b, SparseMatrix) else b
with ops.name_scope(name, "SparseMatrixMatMul", [a_matrix, b_matrix]):
    if isinstance(a, SparseMatrix) and isinstance(b, SparseMatrix):
        if not (isinstance(a, type(b)) or isinstance(b, type(a))):
            raise TypeError("SparseMatrix types don't inherit from each other: "
                            "%s and %s" % (type(a), type(b)))
        c = sm_ops.sparse_matrix_sparse_mat_mul(
            a_matrix,
            b_matrix,
            transpose_a=transpose_a,
            transpose_b=transpose_b,
            adjoint_a=adjoint_a,
            adjoint_b=adjoint_b,
            type=a.dtype)

        # In eager mode, shape inference functions are not called, and the output
        # shape is not set. We have to infer the output shape here.
        # TODO(penporn): Set this from the C++ kernel instead.
        c_handle = matmul_shape_inference(a_matrix, b_matrix, c, transpose_a,
                                          transpose_b, adjoint_a, adjoint_b)
        exit(a._from_matrix(c, handle_data=c_handle))

    elif isinstance(a, SparseMatrix):
        exit(sm_ops.sparse_matrix_mat_mul(
            a_matrix,
            b,
            transpose_a=transpose_a,
            transpose_b=transpose_b,
            adjoint_a=adjoint_a,
            adjoint_b=adjoint_b))
    else:
        # opA(A) . opB(B) = t(nopB(B) . nopA(A))
        if not adjoint_a and not adjoint_b:
            exit(sm_ops.sparse_matrix_mat_mul(
                b_matrix,
                a,
                transpose_a=not transpose_b,
                transpose_b=not transpose_a,
                transpose_output=True))
        elif not transpose_a and not transpose_b:
            exit(sm_ops.sparse_matrix_mat_mul(
                b_matrix,
                a,
                adjoint_a=not adjoint_b,
                adjoint_b=not adjoint_a,
                transpose_output=True,
                conjugate_output=True))
        else:
            exit(sm_ops.sparse_matrix_mat_mul(
                b_matrix,
                math_ops.conj(a),
                transpose_output=True,
                conjugate_output=adjoint_b))
