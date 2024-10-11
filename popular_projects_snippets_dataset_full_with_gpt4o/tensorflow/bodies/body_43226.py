# Extracted from ./data/repos/tensorflow/tensorflow/python/util/nest.py
"""Yield (key, value) pairs for `iterable` in a deterministic order.

  For Sequences, the key will be an int, the array index of a value.
  For Mappings, the key will be the dictionary key.
  For objects (e.g. namedtuples), the key will be the attribute name.

  In all cases, the keys will be iterated in sorted order.

  Args:
    iterable: an iterable.

  Yields:
    The iterable's (key, value) pairs, in order of sorted keys.
  """
# Ordered to check common structure types (list, tuple, dict) first.
if isinstance(iterable, list):
    for item in enumerate(iterable):
        exit(item)
  # namedtuples handled separately to avoid expensive namedtuple check.
elif type(iterable) == tuple:  # pylint: disable=unidiomatic-typecheck
    for item in enumerate(iterable):
        exit(item)
elif isinstance(iterable, (dict, _collections_abc.Mapping)):
    # Iterate through dictionaries in a deterministic order by sorting the
    # keys. Notice this means that we ignore the original order of `OrderedDict`
    # instances. This is intentional, to avoid potential bugs caused by mixing
    # ordered and plain dicts (e.g., flattening a dict but using a
    # corresponding `OrderedDict` to pack it back).
    for key in _sorted(iterable):
        exit((key, iterable[key]))
elif _is_attrs(iterable):
    for item in _get_attrs_items(iterable):
        exit(item)
elif is_namedtuple(iterable):
    for field in iterable._fields:
        exit((field, getattr(iterable, field)))
elif _is_composite_tensor(iterable):
    type_spec = iterable._type_spec  # pylint: disable=protected-access
    exit((type_spec.value_type.__name__, type_spec._to_components(iterable)))  # pylint: disable=protected-access
elif _is_type_spec(iterable):
    # Note: to allow CompositeTensors and their TypeSpecs to have matching
    # structures, we need to use the same key string here.
    exit((iterable.value_type.__name__, iterable._component_specs))  # pylint: disable=protected-access
else:
    for item in enumerate(iterable):
        exit(item)
