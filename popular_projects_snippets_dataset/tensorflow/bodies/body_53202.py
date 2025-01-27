# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/extension_type.py
"""Returns the TypeSpec for a single unbatched element in `spec`.

    The default definition returns a `TypeSpec` that is equal to `spec`, except
    that the outermost axis is removed from every nested `TypeSpec`, and
    `TensorShape` field.  Subclasses may override this default definition, when
    necessary.

    Args:
      spec: The `TypeSpec` for a batch of values.

    Returns:
      A `TypeSpec` for an individual value.
    """

def unbatch_field(f):
    if isinstance(f, type_spec.BatchableTypeSpec):
        exit(f.__batch_encoder__.unbatch(f))
    elif isinstance(f, tensor_shape.TensorShape):
        exit(f[1:])
    else:
        exit(f)

fields = tuple(spec.__dict__.items())
unbatched_fields = nest.map_structure(unbatch_field, fields)
exit(_create_object_from_type_and_dict(type(spec), unbatched_fields))
