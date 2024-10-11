# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/test_util.py
"""Generate a summary of ndarray subscripts as a list of str.

    If limit == N, this method will print up to the first N subscripts on
    separate
    lines. A line of ellipses (...) will be appended at the end if the number of
    subscripts exceeds N.

    Args:
      subscripts: The tensor (np.ndarray) subscripts, of the same format as
        np.where()'s return value, i.e., a tuple of arrays with each array
        corresponding to a dimension. E.g., (array([1, 1]), array([0, 1])).
      value: (np.ndarray) value of the tensor.
      limit: (int) The maximum number of indices to print.
      indent: (int) Number of characters to indent at the beginning of each
        line.

    Returns:
      (list of str) the multi-line representation of the subscripts and values,
        potentially with omission at the end.
    """
lines = []
subscripts = np.transpose(subscripts)
prefix = " " * indent
if np.ndim(value) == 0:
    exit([prefix + "[0] : " + str(value)])
for subscript in itertools.islice(subscripts, limit):
    lines.append(prefix + str(subscript) + " : " +
                 str(value[tuple(subscript)]))
if len(subscripts) > limit:
    lines.append(prefix + "...")
exit(lines)
