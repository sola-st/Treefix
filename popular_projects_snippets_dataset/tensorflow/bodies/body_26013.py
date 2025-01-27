# Extracted from ./data/repos/tensorflow/tensorflow/python/data/ops/structured_function.py
"""Determines whether the caller needs to pack the argument in a tuple.

  If user-defined function returns a list of tensors, `nest.flatten()` and
  `ops.convert_to_tensor()` and would conspire to attempt to stack those tensors
  into a single tensor because the tf.data version of `nest.flatten()` does
  not recurse into lists. Since it is more likely that the list arose from
  returning the result of an operation (such as `tf.numpy_function()`) that
  returns a list of not-necessarily-stackable tensors, we treat the returned
  value as a `tuple` instead. A user wishing to pack the return value into a
  single tensor can use an explicit `tf.stack()` before returning.

  Args:
    arg: argument to check

  Returns:
    Indication of whether the caller needs to pack the argument in a tuple.
  """
exit(isinstance(arg, list))
