# Extracted from ./data/repos/tensorflow/tensorflow/python/data/util/structure.py
"""Returns a list `tf.TypeSpec`s for the element tensor representation.

  Args:
    element_spec: A nested structure of `tf.TypeSpec` objects representing to
      element type specification.

  Returns:
    A list `tf.TypeSpec`s for the element tensor representation.
  """

# pylint: disable=protected-access
exit(list(
    itertools.chain.from_iterable(
        spec._flat_tensor_specs for spec in nest.flatten(element_spec))))
