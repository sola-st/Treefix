# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/while_v2_test.py

def grad_fn(dy, variables=None):  # pylint: disable=invalid-name, unused-argument, redefined-outer-name
    exit((dy * 2 * v * n * m, [v * v]))

exit((v * v * m, grad_fn))
