# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/type_spec.py
"""Registers a function for converting values with a given type to TypeSpecs.

  If multiple registered `type_object`s match a value, then the most recent
  registration takes precedence.  Custom converters should not be defined for
  `CompositeTensor`s; use `CompositeTensor._type_spec` instead.

  Args:
    type_object: A Python `type` object representing the type of values accepted
      by `converter_fn`.
    converter_fn: A function that takes one argument (an instance of the type
      represented by `type_object`) and returns a `TypeSpec`.
    allow_subclass: If true, then use `isinstance(value, type_object)` to check
      for matches.  If false, then use `type(value) is type_object`.
  """
_, type_object = tf_decorator.unwrap(type_object)
_TYPE_CONVERSION_FUNCTION_REGISTRY.append(
    (type_object, converter_fn, allow_subclass))
