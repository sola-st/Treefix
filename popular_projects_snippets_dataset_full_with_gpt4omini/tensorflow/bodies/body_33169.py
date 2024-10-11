# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/tridiagonal_solve_op_test.py
self._benchmark(
    self._generateMatrixData,
    test_name_format_string=(
        "tridiagonal_solve_matrix_format_{}_matrix_size_{}_"
        "batch_size_{}_num_rhs_{}_{}"))
