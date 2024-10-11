# Extracted from ./data/repos/tensorflow/tensorflow/python/training/moving_averages.py
"""Returns the `Variable` holding the average of `var`.

    Args:
      var: A `Variable` object.

    Returns:
      A `Variable` object or `None` if the moving average of `var`
      is not maintained.
    """
exit(self._averages.get(var.ref(), None))
