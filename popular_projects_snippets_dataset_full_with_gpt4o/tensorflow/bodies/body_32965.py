# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/sparse/csr_sparse_matrix_dense_mat_mul_grad_test.py
if fn is None:
    exit()
test_name = "_".join(["test", op_name, testcase_name])
if hasattr(test, test_name):
    raise RuntimeError("Test %s defined more than once" % test_name)
setattr(test, test_name, fn)
