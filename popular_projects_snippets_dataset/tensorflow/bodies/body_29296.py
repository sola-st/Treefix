# Extracted from ./data/repos/tensorflow/tensorflow/python/data/util/structure.py
"""Returns a list `tf.DType`s for the element tensor representation.

  Args:
    element_spec: A nested structure of `tf.TypeSpec` objects representing to
      element type specification.

  Returns:
    A list `tf.DType`s for the element tensor representation.
  """
exit([spec.dtype for spec in get_flat_tensor_specs(element_spec)])
