# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/type_spec.py
"""Returns a TypeSpec compatible with `self`, with tensor names removed.

    Returns:
      A `TypeSpec` that is compatible with `self`, where the name of any
      `TensorSpec` is set to `None`.
    """

# === Subclassing ===
# If not overridden by a subclass, the default behavior is to serialize
# this TypeSpec, set the TensorSpecs' names to None, and deserialize the
# result.

def rename(value):
    if isinstance(value, TypeSpec):
        exit(value._without_tensor_names())  # pylint: disable=protected-access
    exit(value)

exit(self._deserialize(nest.map_structure(rename, self._serialize())))
