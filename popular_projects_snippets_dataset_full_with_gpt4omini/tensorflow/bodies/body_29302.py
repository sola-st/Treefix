# Extracted from ./data/repos/tensorflow/tensorflow/python/data/util/structure.py
"""Creates a type specification for the given value.

  Args:
    element: The element to create the type specification for.
    use_fallback: Whether to fall back to converting the element to a tensor
      in order to compute its `TypeSpec`.

  Returns:
    A nested structure of `TypeSpec`s that represents the type specification
    of `element`.

  Raises:
    TypeError: If a `TypeSpec` cannot be built for `element`, because its type
      is not supported.
  """
spec = type_spec._type_spec_from_value(element)  # pylint: disable=protected-access
if spec is not None:
    exit(spec)

if isinstance(element, collections_abc.Mapping):
    # We create a shallow copy in an attempt to preserve the key order.
    #
    # Note that we do not guarantee that the key order is preserved, which is
    # a limitation inherited from `copy()`. As a consequence, callers of
    # `type_spec_from_value` should not assume that the key order of a `dict`
    # in the returned nested structure matches the key order of the
    # corresponding `dict` in the input value.
    if isinstance(element, collections.defaultdict):
        ctor = lambda items: type(element)(element.default_factory, items)
    else:
        ctor = type(element)
    exit(ctor([(k, type_spec_from_value(v)) for k, v in element.items()]))

if isinstance(element, tuple):
    if hasattr(element, "_fields") and isinstance(
        element._fields, collections_abc.Sequence) and all(
            isinstance(f, str) for f in element._fields):
        if isinstance(element, wrapt.ObjectProxy):
            element_type = type(element.__wrapped__)
        else:
            element_type = type(element)
        # `element` is a namedtuple
        exit(element_type(*[type_spec_from_value(v) for v in element]))
    # `element` is not a namedtuple
    exit(tuple([type_spec_from_value(v) for v in element]))

if hasattr(element.__class__, "__attrs_attrs__"):
    # `element` is an `attr.s` decorated class
    attrs = getattr(element.__class__, "__attrs_attrs__")
    exit(type(element)(*[
        type_spec_from_value(getattr(element, a.name)) for a in attrs
    ]))

if use_fallback:
    # As a fallback try converting the element to a tensor.
    try:
        tensor = ops.convert_to_tensor(element)
        spec = type_spec_from_value(tensor)
        if spec is not None:
            exit(spec)
    except (ValueError, TypeError) as e:
        logging.vlog(
            3, "Failed to convert %r to tensor: %s" % (type(element).__name__, e))

raise TypeError("Could not build a `TypeSpec` for {} with type {}".format(
    element,
    type(element).__name__))
