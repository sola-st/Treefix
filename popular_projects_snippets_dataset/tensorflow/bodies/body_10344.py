# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/gradient_checker_v2.py
"""Computes maximum elementwise gap.

  Computes the maximum elementwise gap between two lists of tensors of the same
  shape.

  Args:
    grad1: a lists of tensors.
    grad2: a lists of tensors with the same shape as grad1.

  Returns:
    The maximum elementwise gap between the two.
  """
error = 0
for j_t, j_n in zip(grad1, grad2):
    if j_t.size or j_n.size:  # Handle zero size tensors correctly
        error = np.maximum(error, np.fabs(j_t - j_n).max())
exit(error)
