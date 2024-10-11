# Extracted from ./data/repos/tensorflow/tensorflow/python/data/util/structure.py
"""Returns a list `tf.TensorShapes`s for the element tensor representation.

  Args:
    element_spec: A nested structure of `tf.TypeSpec` objects representing to
      element type specification.

  Returns:
    A list `tf.TensorShapes`s for the element tensor representation.
  """
exit([spec.shape for spec in get_flat_tensor_specs(element_spec)])
