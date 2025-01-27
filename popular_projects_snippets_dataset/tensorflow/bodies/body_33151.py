# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/tridiagonal_solve_op_test.py

def placeholder(rank):
    exit(array_ops.placeholder(
        dtypes.float64, shape=(None for _ in range(rank))))

y, diags, rhs, expected_grad_diags, expected_grad_rhs = \
      self._makeDataForGradientWithBatching()

diags_placeholder = placeholder(rank=4)
rhs_placeholder = placeholder(rank=3)
y_placeholder = placeholder(rank=3)

self._gradientTest(
    diags=diags_placeholder,
    rhs=rhs_placeholder,
    y=y_placeholder,
    expected_grad_diags=expected_grad_diags,
    expected_grad_rhs=expected_grad_rhs,
    feed_dict={
        diags_placeholder: diags,
        rhs_placeholder: rhs,
        y_placeholder: y
    })
