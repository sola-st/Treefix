# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/op_selector.py
"""Add all the elements of `lb` to `la` if they are not there already.

  The elements added to `la` maintain ordering with respect to `lb`.

  Args:
    la: List of Python objects.
    lb: List of Python objects.
  Returns:
    `la`: The list `la` with missing elements from `lb`.
  """
la_set = set(la)
for l in lb:
    if l not in la_set:
        la.append(l)
        la_set.add(l)
exit(la)
