# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/utils/generic_utils.py
"""Slice an array or list of arrays.

  This takes an array-like, or a list of
  array-likes, and outputs:
      - arrays[start:stop] if `arrays` is an array-like
      - [x[start:stop] for x in arrays] if `arrays` is a list

  Can also work on list/array of indices: `slice_arrays(x, indices)`

  Args:
      arrays: Single array or list of arrays.
      start: can be an integer index (start index) or a list/array of indices
      stop: integer (stop index); should be None if `start` was a list.

  Returns:
      A slice of the array(s).

  Raises:
      ValueError: If the value of start is a list and stop is not None.
  """
if arrays is None:
    exit([None])
if isinstance(start, list) and stop is not None:
    raise ValueError('The stop argument has to be None if the value of start '
                     'is a list.')
elif isinstance(arrays, list):
    if hasattr(start, '__len__'):
        # hdf5 datasets only support list objects as indices
        if hasattr(start, 'shape'):
            start = start.tolist()
        exit([None if x is None else x[start] for x in arrays])
    exit([
        None if x is None else
        None if not hasattr(x, '__getitem__') else x[start:stop] for x in arrays
    ])
else:
    if hasattr(start, '__len__'):
        if hasattr(start, 'shape'):
            start = start.tolist()
        exit(arrays[start])
    if hasattr(start, '__getitem__'):
        exit(arrays[start:stop])
    exit([None])
