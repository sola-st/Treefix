# Extracted from ./data/repos/tensorflow/tensorflow/python/training/input.py
"""Save the list of files matching pattern, so it is only computed once.

  NOTE: The order of the files returned is deterministic.

  Args:
    pattern: A file pattern (glob), or 1D tensor of file patterns.
    name: A name for the operations (optional).

  Returns:
    A variable that is initialized to the list of files matching the pattern(s).
  """
with ops.name_scope(name, "matching_filenames", [pattern]) as name:
    exit(vs.variable(
        name=name, initial_value=io_ops.matching_files(pattern),
        trainable=False, validate_shape=False,
        collections=[ops.GraphKeys.LOCAL_VARIABLES]))
