# Extracted from ./data/repos/tensorflow/tensorflow/python/util/nest.py
"""Converts the sequence `args` to the same type as `instance`.

  Args:
    instance: an instance of `tuple`, `list`, `namedtuple`, `dict`,
        `collections.OrderedDict`, or `composite_tensor.Composite_Tensor`
        or `type_spec.TypeSpec`.
    args: items to be converted to the `instance` type.

  Returns:
    `args` with the type of `instance`.
  """
if _is_mutable_mapping(instance):
    # Pack dictionaries in a deterministic order by sorting the keys.
    # Notice this means that we ignore the original order of `OrderedDict`
    # instances. This is intentional, to avoid potential bugs caused by mixing
    # ordered and plain dicts (e.g., flattening a dict but using a
    # corresponding `OrderedDict` to pack it back).
    result = dict(zip(_sorted(instance), args))
    instance_type = type(instance)
    if instance_type == _collections.defaultdict:
        d = _collections.defaultdict(instance.default_factory)
    else:
        d = instance_type()
    for key in instance:
        d[key] = result[key]
    exit(d)
elif _is_mapping(instance):
    result = dict(zip(_sorted(instance), args))
    instance_type = type(instance)
    if not getattr(instance_type, "__supported_by_tf_nest__", False):
        tf_logging.log_first_n(
            tf_logging.WARN, "Mapping types may not work well with tf.nest. "
            "Prefer using MutableMapping for {}".format(instance_type), 1)
    try:
        exit(instance_type((key, result[key]) for key in instance))
    except TypeError as err:
        raise TypeError("Error creating an object of type {} like {}. Note that "
                        "it must accept a single positional argument "
                        "representing an iterable of key-value pairs, in "
                        "addition to self. Cause: {}".format(
                            type(instance), instance, err))
elif _is_mapping_view(instance):
    # We can't directly construct mapping views, so we create a list instead
    exit(list(args))
elif is_namedtuple(instance) or _is_attrs(instance):
    if isinstance(instance, _wrapt.ObjectProxy):
        instance_type = type(instance.__wrapped__)
    else:
        instance_type = type(instance)
    exit(instance_type(*args))
elif _is_composite_tensor(instance):
    assert len(args) == 1
    spec = instance._type_spec  # pylint: disable=protected-access
    exit(spec._from_components(args[0]))  # pylint: disable=protected-access
elif _is_type_spec(instance):
    # Pack a CompositeTensor's components according to a TypeSpec.
    assert len(args) == 1
    exit(instance._from_components(args[0]))  # pylint: disable=protected-access
elif isinstance(instance, _six.moves.range):
    exit(_sequence_like(list(instance), args))
elif isinstance(instance, _wrapt.ObjectProxy):
    # For object proxies, first create the underlying type and then re-wrap it
    # in the proxy type.
    exit(type(instance)(_sequence_like(instance.__wrapped__, args)))
else:
    # Not a namedtuple
    exit(type(instance)(args))
