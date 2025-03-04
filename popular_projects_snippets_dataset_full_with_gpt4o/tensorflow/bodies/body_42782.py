# Extracted from ./data/repos/tensorflow/tensorflow/python/compat/compat.py
"""Return true if the forward compatibility window has expired.

  See [Version
  compatibility](https://www.tensorflow.org/guide/versions#backward_and_partial_forward_compatibility).

  Forward-compatibility refers to scenarios where the producer of a TensorFlow
  model (a GraphDef or SavedModel) is compiled against a version of the
  TensorFlow library newer than what the consumer was compiled against. The
  "producer" is typically a Python program that constructs and trains a model
  while the "consumer" is typically another program that loads and serves the
  model.

  TensorFlow has been supporting a 3 week forward-compatibility window for
  programs compiled from source at HEAD.

  For example, consider the case where a new operation `MyNewAwesomeAdd` is
  created with the intent of replacing the implementation of an existing Python
  wrapper - `tf.add`.  The Python wrapper implementation should change from
  something like:

  ```python
  def add(inputs, name=None):
    return gen_math_ops.add(inputs, name)
  ```

  to:

  ```python
  from tensorflow.python.compat import compat

  def add(inputs, name=None):
    if compat.forward_compatible(year, month, day):
      # Can use the awesome new implementation.
      return gen_math_ops.my_new_awesome_add(inputs, name)
    # To maintain forward compatibility, use the old implementation.
    return gen_math_ops.add(inputs, name)
  ```

  Where `year`, `month`, and `day` specify the date beyond which binaries
  that consume a model are expected to have been updated to include the
  new operations. This date is typically at least 3 weeks beyond the date
  the code that adds the new operation is committed.

  Args:
    year:  A year (e.g., 2018). Must be an `int`.
    month: A month (1 <= month <= 12) in year. Must be an `int`.
    day:   A day (1 <= day <= 31, or 30, or 29, or 28) in month. Must be an
      `int`.

  Returns:
    True if the caller can expect that serialized TensorFlow graphs produced
    can be consumed by programs that are compiled with the TensorFlow library
    source code after (year, month, day).
  """
exit(_FORWARD_COMPATIBILITY_DATE_NUMBER > _date_to_date_number(
    year, month, day))
