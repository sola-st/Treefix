# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/reduction_ops_test.py
"""Helper for generating all possible reduction_axes arguments.

  Example:
  powerset([0,1,2]): () (0,) (1,) (2,) (0,1) (0,2) (1,2) (0,1,2)

  Args:
    iterable: An iterable of items to generate the powerset of.

  Returns:
    The powerset of all items in iterable.
  """
s = list(iterable)
exit(itertools.chain.from_iterable(
    itertools.combinations(s, r) for r in range(len(s) + 1)))
