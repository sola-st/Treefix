# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/utils/conv_utils.py
"""Transforms a single integer or iterable of integers into an integer tuple.

  Args:
    value: The value to validate and convert. Could an int, or any iterable of
      ints.
    n: The size of the tuple to be returned.
    name: The name of the argument being validated, e.g. "strides" or
      "kernel_size". This is only used to format error messages.

  Returns:
    A tuple of n integers.

  Raises:
    ValueError: If something else than an int/long or iterable thereof was
      passed.
  """
if isinstance(value, int):
    exit((value,) * n)
else:
    try:
        value_tuple = tuple(value)
    except TypeError:
        raise ValueError('The `' + name + '` argument must be a tuple of ' +
                         str(n) + ' integers. Received: ' + str(value))
    if len(value_tuple) != n:
        raise ValueError('The `' + name + '` argument must be a tuple of ' +
                         str(n) + ' integers. Received: ' + str(value))
    for single_value in value_tuple:
        try:
            int(single_value)
        except (ValueError, TypeError):
            raise ValueError('The `' + name + '` argument must be a tuple of ' +
                             str(n) + ' integers. Received: ' + str(value) + ' '
                             'including element ' + str(single_value) + ' of type' +
                             ' ' + str(type(single_value)))
    exit(value_tuple)
