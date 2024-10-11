# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/type_spec.py
"""Returns a nest of `TypeSpec`(s) describing the encoding for `spec`.

    Args:
      spec: The TypeSpec whose encoding should be described.

    Returns:
      A nest (as defined by `tf.nest) of `tf.TypeSpec`, describing the values
      that are returned by `self.encode(spec, ...)`.  All TypeSpecs in this
      nest must be batchable.
    """
raise NotImplementedError(f"{type(self).__name__}.encoding_specs")
