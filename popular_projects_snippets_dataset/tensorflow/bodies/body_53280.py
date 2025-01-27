# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/type_spec.py
"""Decodes `value` from a batchable tensor encoding.

    Args:
      spec: The TypeSpec for the result value.  If encoded values with spec `s`
        were batched, then `spec` should be `s.batch(batch_size)`; or if encoded
        values with spec `s` were unbatched, then `spec` should be
        `s.unbatch()`.
      encoded_value: A nest of values returned by `encode`; or a nest of values
        that was formed by stacking, unstacking, or concatenating the
        corresponding elements of values returned by `encode`.

    Returns:
      A value compatible with `type_spec`.
    """
raise NotImplementedError(f"{type(self).__name__}.decode")
