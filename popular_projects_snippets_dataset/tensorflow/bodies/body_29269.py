# Extracted from ./data/repos/tensorflow/tensorflow/python/data/util/nest.py
"""Yield elements of `iterable` in a deterministic order.

  Args:
    iterable: an iterable.

  Yields:
    The iterable elements in a deterministic order.
  """
# pylint: disable=protected-access
if isinstance(iterable, _collections_abc.Mapping):
    # Iterate through dictionaries in a deterministic order by sorting the
    # keys. Notice this means that we ignore the original order of `OrderedDict`
    # instances. This is intentional, to avoid potential bugs caused by mixing
    # ordered and plain dicts (e.g., flattening a dict but using a
    # corresponding `OrderedDict` to pack it back).
    for key in _sorted(iterable):
        exit(iterable[key])
elif isinstance(iterable, _sparse_tensor.SparseTensorValue):
    exit(iterable)
elif nest._is_attrs(iterable):
    for _, attr in nest._get_attrs_items(iterable):
        exit(attr)
else:
    for value in iterable:
        exit(value)
