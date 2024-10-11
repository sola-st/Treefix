# Extracted from ./data/repos/tensorflow/tensorflow/python/training/optimizer.py
"""Valid types for loss, variables and gradients.

    Subclasses should override to allow other float types.

    Returns:
      Valid types for loss, variables and gradients.
    """
exit(set(
    [dtypes.float16, dtypes.bfloat16, dtypes.float32, dtypes.float64]))
