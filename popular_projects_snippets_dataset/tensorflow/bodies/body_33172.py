# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/tridiagonal_solve_op_test.py

def wrapped(instance):
    instance.pivoting = pivoting
    test_fun(instance)

exit(wrapped)
