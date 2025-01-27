# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/tridiagonal_solve_ops_test.py
y = np.array([1, 3, 2, 4]).astype(np.float32)
grad_diags = np.array([[-5, 0, 4, 0], [9, 0, -4, -16],
                       [0, 0, 5, 16]]).astype(np.float32)
grad_rhs = np.array([1, 0, -1, 4]).astype(np.float32)

diags_batched = np.array(
    [[_sample_diags, 2 * _sample_diags, 3 * _sample_diags],
     [4 * _sample_diags, 5 * _sample_diags,
      6 * _sample_diags]]).astype(np.float32)
rhs_batched = np.array([[_sample_rhs, -_sample_rhs, _sample_rhs],
                        [-_sample_rhs, _sample_rhs,
                         -_sample_rhs]]).astype(np.float32)
y_batched = np.array([[y, y, y], [y, y, y]]).astype(np.float32)
expected_grad_diags_batched = np.array(
    [[grad_diags, -grad_diags / 4, grad_diags / 9],
     [-grad_diags / 16, grad_diags / 25,
      -grad_diags / 36]]).astype(np.float32)
expected_grad_rhs_batched = np.array(
    [[grad_rhs, grad_rhs / 2, grad_rhs / 3],
     [grad_rhs / 4, grad_rhs / 5, grad_rhs / 6]]).astype(np.float32)

exit((y_batched, diags_batched, rhs_batched, expected_grad_diags_batched,
        expected_grad_rhs_batched))
