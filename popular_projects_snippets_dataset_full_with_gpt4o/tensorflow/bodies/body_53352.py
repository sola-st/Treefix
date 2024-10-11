# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops.py
"""Dummy method to prevent a tensor from being used as a Python `bool`.

    This overload raises a `TypeError` when the user inadvertently
    treats a `Tensor` as a boolean (most commonly in an `if` or `while`
    statement), in code that was not converted by AutoGraph. For example:

    ```python
    if tf.constant(True):  # Will raise.
      # ...

    if tf.constant(5) < tf.constant(7):  # Will raise.
      # ...
    ```

    Raises:
      `TypeError`.
    """
self._disallow_bool_casting()
