# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops.py
"""EXPERIMENTAL: A context manager for overriding gradient functions.

    This context manager can be used to override the gradient function
    that will be used for ops within the scope of the context.

    For example:

    ```python
    @tf.RegisterGradient("CustomSquare")
    def _custom_square_grad(op, grad):
      # ...

    with tf.Graph().as_default() as g:
      c = tf.constant(5.0)
      s_1 = tf.square(c)  # Uses the default gradient for tf.square.
      with g.gradient_override_map({"Square": "CustomSquare"}):
        s_2 = tf.square(s_2)  # Uses _custom_square_grad to compute the
                              # gradient of s_2.
    ```

    Args:
      op_type_map: A dictionary mapping op type strings to alternative op type
        strings.

    Returns:
      A context manager that sets the alternative op type to be used for one
      or more ops created in that context.

    Raises:
      TypeError: If `op_type_map` is not a dictionary mapping strings to
        strings.
    """
if not isinstance(op_type_map, dict):
    raise TypeError("op_type_map must be a dictionary mapping "
                    "strings to strings")
# The saved_mappings dictionary stores any currently-set mappings that
# will be overridden by this context manager.
saved_mappings = {}
# Install the given label
for op_type, mapped_op_type in op_type_map.items():
    if not (isinstance(op_type, str) and
            isinstance(mapped_op_type, str)):
        raise TypeError("op_type_map must be a dictionary mapping "
                        "strings to strings")
    try:
        saved_mappings[op_type] = self._gradient_override_map[op_type]
    except KeyError:
        pass
    self._gradient_override_map[op_type] = mapped_op_type
try:
    exit()  # The code within the context runs here.
finally:
    # Remove the labels set for this context, and restore any saved labels.
    for op_type, mapped_op_type in op_type_map.items():
        try:
            self._gradient_override_map[op_type] = saved_mappings[op_type]
        except KeyError:
            del self._gradient_override_map[op_type]
