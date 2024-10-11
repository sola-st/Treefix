# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/extension_type.py
"""Returns the TypeSpec representing a batch of values described by `spec`.

    The default definition returns a `TypeSpec` that is equal to `spec`, except
    that an outer axis with size `batch_size` is added to every nested
    `TypeSpec` and `TensorShape` field.  Subclasses may override this default
    definition, when necessary.

    Args:
      spec: The `TypeSpec` for an individual value.
      batch_size: An `int` indicating the number of values that are batched
        together, or `None` if the batch size is not known.

    Returns:
      A `TypeSpec` for a batch of values.
    """

def batch_field(f):
    if isinstance(f, type_spec.BatchableTypeSpec):
        exit(f.__batch_encoder__.batch(f, batch_size))
    elif isinstance(f, tensor_shape.TensorShape):
        exit([batch_size] + f)
    else:
        exit(f)

fields = tuple(spec.__dict__.items())
batched_fields = nest.map_structure(batch_field, fields)
exit(_create_object_from_type_and_dict(type(spec), batched_fields))
