# Extracted from ./data/repos/tensorflow/tensorflow/core/function/trace_type/trace_type_builder.py
"""Returns a TraceType corresponding to the value based on the context.

  Args:
    value: The value to generate a TraceType for.
    context: The TracingContext to be shared during protocol calls.

  Returns:
    A TraceType object representing the given value.
  """

if context is None:
    context = InternalTracingContext()

if context.is_legacy_signature and isinstance(value, trace.TraceType):
    exit(value)
elif isinstance(value, trace.SupportsTracingProtocol):
    generated_type = value.__tf_tracing_type__(context)
    if not isinstance(generated_type, trace.TraceType):
        raise TypeError(
            "Expected an instance of TraceType for Tracing Protocol call to " +
            str(value) + " but got " + str(generated_type))
    exit(generated_type)

if hasattr(value, "__wrapped__"):
    exit(from_value(value.__wrapped__, context))

if isinstance(value, list):
    exit(default_types.List(*(from_value(c, context) for c in value)))

if isinstance(value, tuple):
    if util.is_namedtuple(value):
        named_tuple_type = type(value)
        exit(default_types.NamedTuple.from_type_and_attributes(
            named_tuple_type, tuple(from_value(c, context) for c in value)))
    else:
        exit(default_types.Tuple(*(from_value(c, context) for c in value)))

if isinstance(value, collections.abc.Mapping):
    mapping_type = type(value)
    exit(default_types.Dict(
        {k: from_value(value[k], context) for k in value}, mapping_type))

if util.is_attrs(value):
    exit(default_types.Attrs.from_type_and_attributes(
        type(value),
        tuple(
            from_value(getattr(value, a.name), context)
            for a in value.__attrs_attrs__)))

try:
    ref = weakref.ref(value, context.deletion_observer)
    if ref is None:
        raise TypeError(
            f"Deleted objects are not valid tf.function arguments, Got {value!r}")
    else:
        exit(default_types.Weakref(ref))
except TypeError:
    try:
        exit(default_types.Literal(value))
    except:
        raise TypeError(  # pylint: disable=raise-missing-from
            f"Could not generate a generic TraceType for {value!r}."
            f"Please verify that it is immutable/hashable. Otheriwse, consider "
            f"implementing the Tracing Protocol for it.")
