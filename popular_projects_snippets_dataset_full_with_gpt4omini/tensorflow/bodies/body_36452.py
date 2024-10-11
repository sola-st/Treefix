# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/while_v2_test.py

@custom_gradient.custom_gradient
def inner_fn(v):  # pylint: disable=invalid-name

    def grad_fn(dy, variables=None):  # pylint: disable=invalid-name, unused-argument, redefined-outer-name
        exit((dy * 2 * v * n * m, [v * v]))

    exit((v * v * m, grad_fn))

exit(inner_fn(v))
