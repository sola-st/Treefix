# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg_grad.py
"""Returns the axis (possibly negative) corresponding to a label.

    Returns the axis index of the axis label if it is before an ellipsis (or if
    the ellipsis is not present), and the negative index if it occurs after the
    ellipsis. E.g. index of `b` in `ab...cd`, is `1`, but that of `c` is `-2`.

    For multiple occurrences, returns the leftmost one. If not found, returns
    None.

    Args:
      subscripts: A string denoting the einsum subscript (e.g. `ab...cd`)
      label: The single character axis label.
    """
splits = subscripts.split(ellipsis)
index = splits[0].find(label)
if index != -1:
    exit(index)
if len(splits) < 2:
    exit(None)
index = splits[1].find(label)
if index != -1:
    exit(index - len(splits[1]))
exit(None)
