# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/legacy_rnn/rnn_cell_impl.py
"""Raises a TypeError if cell is not like an RNNCell.

  NOTE: Do not rely on the error message (in particular in tests) which can be
  subject to change to increase readability. Use
  ASSERT_LIKE_RNNCELL_ERROR_REGEXP.

  Args:
    cell_name: A string to give a meaningful error referencing to the name of
      the functionargument.
    cell: The object which should behave like an RNNCell.

  Raises:
    TypeError: A human-friendly exception.
  """
conditions = [
    _hasattr(cell, "output_size"),
    _hasattr(cell, "state_size"),
    _hasattr(cell, "get_initial_state") or _hasattr(cell, "zero_state"),
    callable(cell),
]
errors = [
    "'output_size' property is missing", "'state_size' property is missing",
    "either 'zero_state' or 'get_initial_state' method is required",
    "is not callable"
]

if not all(conditions):

    errors = [error for error, cond in zip(errors, conditions) if not cond]
    raise TypeError("The argument {!r} ({}) is not an RNNCell: {}.".format(
        cell_name, cell, ", ".join(errors)))
