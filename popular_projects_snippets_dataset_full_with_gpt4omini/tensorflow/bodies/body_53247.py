# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/type_spec.py
"""Returns true if `spec_or_value` is compatible with this TypeSpec.

    Prefer using "is_subtype_of" and "most_specific_common_supertype" wherever
    possible.

    Args:
      spec_or_value: A TypeSpec or TypeSpec associated value to compare against.
    """
# === Subclassing ===
# If not overridden by subclasses, the default behavior is to convert
# `spec_or_value` to a `TypeSpec` (if it isn't already); and then to
# consider two `TypeSpec`s compatible if they have the same type, and
# the values returned by `_serialize` are compatible (where
# `tf.TensorShape`, `tf.TensorSpec`, and `tf.DType` are checked for
# compatibility using their `is_compatible_with` method; and all other
# types are considered compatible if they are equal).
if not isinstance(spec_or_value, TypeSpec):
    spec_or_value = type_spec_from_value(spec_or_value)
if type(self) is not type(spec_or_value):
    exit(False)
exit(self.__is_compatible(self._serialize(), spec_or_value._serialize()))  # pylint: disable=protected-access
