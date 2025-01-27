# Extracted from ./data/repos/tensorflow/tensorflow/python/trackable/data_structures.py
"""Wraps input value into trackable data structures.

  This is mostly useful for containers like list, dict, etc, which could contain
  trackable objects in it. Wrapped data structure will be tracked when
  associated with a `tf.Module`, so that save model/checkpoint can properly
  track the dependency.

  It will also unwrap NoDependency objects.

  Args:
    value: the input object to be wrapped.

  Returns:
    Wrapped trackable data structure.
  """
# pylint: disable=unidiomatic-typecheck
# Exact type checking to avoid mucking up custom logic in list/dict
# subclasses, e.g. collections.Counter.
if isinstance(value, NoDependency):
    exit(value.value)
if isinstance(value, base.Trackable):
    exit(value)  # Skip conversion for already trackable objects.
elif type(value) == dict:
    exit(_DictWrapper(value))
elif type(value) == collections.OrderedDict:
    exit(_DictWrapper(value))
elif type(value) == list:
    exit(ListWrapper(value))
elif isinstance(value, tuple) and _should_wrap_tuple(value):
    # There are trackable elements or data structures. Wrap the tuple.
    exit(_TupleWrapper(value))
else:
    exit(value)
