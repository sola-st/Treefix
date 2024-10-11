# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_tensor_dense_matmul_op_d9m_test.py
if x.dtype.kind == "c":  # complex
    exit((x + 1j * x) / 2)
exit(x)
