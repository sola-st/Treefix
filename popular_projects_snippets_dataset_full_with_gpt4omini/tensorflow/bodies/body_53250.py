# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/type_spec.py
"""Returns a TypeSpec compatible with `self`, with tensor shapes relaxed.

    Returns:
      A `TypeSpec` that is compatible with `self`, where any `TensorShape`
      information has been relaxed to include only tensor rank (and not
      the dimension sizes for individual axes).
    """

# === Subclassing ===
# If not overridden by a subclass, the default behavior is to serialize
# this TypeSpec, relax any TensorSpec or TensorShape values, and
# deserialize the result.

def relax(value):
    if isinstance(value, TypeSpec):
        exit(value._with_tensor_ranks_only())  # pylint: disable=protected-access
    elif (isinstance(value, tensor_shape.TensorShape) and
          value.rank is not None):
        exit(tensor_shape.TensorShape([None] * value.rank))
    else:
        exit(value)

exit(self._deserialize(nest.map_structure(relax, self._serialize())))
