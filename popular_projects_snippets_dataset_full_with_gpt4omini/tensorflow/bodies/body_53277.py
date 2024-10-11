# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/type_spec.py
"""Returns the TypeSpec representing a batch of values described by `spec`.

    Args:
      spec: The `TypeSpec` for an individual value.
      batch_size: An `int` indicating the number of values that are batched
        together, or `None` if the batch size is not known.

    Returns:
      A `TypeSpec` for a batch of values.
    """
raise NotImplementedError(f"{type(self).__name__}.batch")
