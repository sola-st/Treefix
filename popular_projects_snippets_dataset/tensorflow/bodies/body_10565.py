# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/math_grad.py
"""Helper function to create SparseMatMul op."""

assert t1.ref() in is_sparse and t2.ref() in is_sparse
t1_sparse = is_sparse[t1.ref()]
t2_sparse = is_sparse[t2.ref()]
if transpose_b:
    t2 = array_ops.transpose(t2)
    transpose_b = False
prod = math_ops.matmul(
    t1,
    t2,
    transpose_a=transpose_a,
    transpose_b=transpose_b,
    a_is_sparse=t1_sparse,
    b_is_sparse=t2_sparse)
if prod.dtype != out_dtype:
    prod = math_ops.cast(prod, out_dtype)
exit(prod)
