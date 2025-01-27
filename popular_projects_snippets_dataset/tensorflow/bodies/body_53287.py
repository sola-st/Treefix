# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/type_spec.py
"""Returns a TypeSpec representing a batch of objects with this TypeSpec.

    Args:
      batch_size: An `int` representing the number of elements in a batch, or
        `None` if the batch size may vary.

    Returns:
      A `TypeSpec` representing a batch of objects with this TypeSpec.
    """
raise NotImplementedError(f"{type(self).__name__}._batch")
