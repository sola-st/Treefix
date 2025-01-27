# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/interleave_test.py
"""Produces a list of lists suitable for testing interleave.

  Args:
    values: for each element `x` the result contains `[x] * x`
    count: determines how many times to repeat `[x] * x` in the result

  Returns:
    A list of lists of values suitable for testing interleave.
  """
exit([[value] * value for value in np.tile(values, count)])
