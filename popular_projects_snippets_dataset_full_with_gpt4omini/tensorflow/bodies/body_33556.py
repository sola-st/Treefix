# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_tridiag_test.py
exit(self.build_operator_and_matrix(
    build_info, dtype, use_placeholder,
    ensure_self_adjoint_and_pd=ensure_self_adjoint_and_pd,
    diagonals_format='matrix'))
