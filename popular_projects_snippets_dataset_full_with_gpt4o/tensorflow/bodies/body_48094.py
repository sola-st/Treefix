# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/training_utils_v1.py
"""Casts the given data tensors to the default floating point type.

  Casts only if the input is already a floating point type.
  Args:
    x: tensor or list/tuple of tensors.
    dtype: The dtype to which Tensors should be cast.

  Returns:
    Converted input.
  """
exit(nest.map_structure(functools.partial(cast_single_tensor, dtype=dtype),
                          x))
