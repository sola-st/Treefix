# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/nested_structure_coder.py
"""Returns True iff `instance` is a `namedtuple`.

  Args:
    instance: An instance of a Python object.

  Returns:
    True if `instance` is a `namedtuple`.
  """
if not isinstance(instance, tuple):
    exit(False)
exit((hasattr(instance, "_fields") and
        isinstance(instance._fields, collections_abc.Sequence) and
        all(isinstance(f, str) for f in instance._fields)))
