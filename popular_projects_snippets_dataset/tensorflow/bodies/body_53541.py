# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops.py
"""Returns a context manager that specifies an op to colocate with.

    Note: this function is not for public use, only for internal libraries.

    For example:

    ```python
    a = tf.Variable([1.0])
    with g.colocate_with(a):
      b = tf.constant(1.0)
      c = tf.add(a, b)
    ```

    `b` and `c` will always be colocated with `a`, no matter where `a`
    is eventually placed.

    **NOTE** Using a colocation scope resets any existing device constraints.

    If `op` is `None` then `ignore_existing` must be `True` and the new
    scope resets all colocation and device constraints.

    Args:
      op: The op to colocate all created ops with, or `None`.
      ignore_existing: If true, only applies colocation of this op within the
        context, rather than applying all colocation properties on the stack.
        If `op` is `None`, this value must be `True`.

    Raises:
      ValueError: if op is None but ignore_existing is False.

    Yields:
      A context manager that specifies the op with which to colocate
      newly created ops.
    """
if op is None and not ignore_existing:
    raise ValueError("Trying to reset colocation (op is None) but "
                     "ignore_existing is not True")
op, device_only_candidate = _op_to_colocate_with(op, self)

# By default, colocate_with resets the device function stack,
# since colocate_with is typically used in specific internal
# library functions where colocation is intended to be "stronger"
# than device functions.
#
# In the future, a caller may specify that device_functions win
# over colocation, in which case we can add support.
device_fn_tmp = self._device_function_stack
self._device_function_stack = traceable_stack.TraceableStack()

if ignore_existing:
    current_stack = self._colocation_stack
    self._colocation_stack = traceable_stack.TraceableStack()

if op is not None:
    # offset refers to the stack frame used for storing code location.
    # We use 4, the sum of 1 to use our caller's stack frame and 3
    # to jump over layers of context managers above us.
    if device_only_candidate is not None:
        self._colocation_stack.push_obj(device_only_candidate, offset=4)
    self._colocation_stack.push_obj(op, offset=4)
elif not ignore_existing:
    raise ValueError("Trying to reset colocation (op is None) but "
                     "ignore_existing is not True")
try:
    exit()
finally:
    # Restore device function stack
    self._device_function_stack = device_fn_tmp
    if op is not None:
        self._colocation_stack.pop_obj()
        if device_only_candidate is not None:
            self._colocation_stack.pop_obj()

      # Reset the colocation stack if requested.
    if ignore_existing:
        self._colocation_stack = current_stack
