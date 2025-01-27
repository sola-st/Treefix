# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/cross_device_utils.py
"""Stitch values together according to their indices.

  Args:
    values_and_indices_list: a list of tuples of values and indices indicating
      the values and positions in the returned list.

  Returns:
    a stitched list of values.
  """
length = 0
for values_and_indices in values_and_indices_list:
    length += len(values_and_indices[0])

result = [None] * length
for values_and_indices in values_and_indices_list:
    if values_and_indices and values_and_indices[0]:
        for v, i in zip(*values_and_indices):
            assert result[i] is None
            result[i] = v
exit(result)
