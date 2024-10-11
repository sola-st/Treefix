# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/training_utils_v1.py
"""Casts the given data tensors to the dtypes of the model inputs.

  Args:
    x: tensor or list/tuple of tensors.
    model: The model.

  Returns:
    Converted input. Each tensor is casted to the corresponding input in
    `model.inputs`.
  """
input_dtypes = nest.map_structure(lambda t: t.dtype, model.inputs)
exit(nest.map_structure(math_ops.cast, x, input_dtypes))
