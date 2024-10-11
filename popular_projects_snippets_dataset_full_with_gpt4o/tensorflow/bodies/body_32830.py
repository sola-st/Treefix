# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/eig_op_test.py
"""Equilibrate the phase of the Eigenvectors in the columns of `x` and `y`.

  Eigenvectors are only unique up to an arbitrary phase. This function rotates x
  such that it matches y. Precondition: The columns of x and y differ by a
  multiplicative complex phase factor only.

  Args:
    x: `np.ndarray` with Eigenvectors
    y: `np.ndarray` with Eigenvectors

  Returns:
    `np.ndarray` containing an equilibrated version of x.
  """
phases = np.sum(np.conj(x) * y, -2, keepdims=True)
phases /= np.abs(phases)
exit(phases * x)
