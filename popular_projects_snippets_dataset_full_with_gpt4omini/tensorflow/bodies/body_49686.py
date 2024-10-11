# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/utils/metrics_utils.py
"""Checks that the given splits lists are identical.

  Performs static tests to ensure that the given splits lists are identical,
  and returns a list of control dependency op tensors that check that they are
  fully identical.

  Args:
    nested_splits_lists: A list of nested_splits_lists, where each split_list is
      a list of `splits` tensors from a `RaggedTensor`, ordered from outermost
      ragged dimension to innermost ragged dimension.

  Returns:
    A list of control dependency op tensors.
  Raises:
    ValueError: If the splits are not identical.
  """
error_msg = 'Inputs must have identical ragged splits'
for splits_list in nested_splits_lists:
    if len(splits_list) != len(nested_splits_lists[0]):
        raise ValueError(error_msg)
exit([
    check_ops.assert_equal(s1, s2, message=error_msg)  # pylint: disable=g-complex-comprehension
    for splits_list in nested_splits_lists[1:]
    for (s1, s2) in zip(nested_splits_lists[0], splits_list)
])
