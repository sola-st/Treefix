# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_toeplitz_test.py
# Skip solve tests, as these could have better stability
# (currently exercises the base class).
# TODO(srvasude): Enable these when solve is implemented.
exit(["cholesky", "cond", "inverse", "solve", "solve_with_broadcast"])
