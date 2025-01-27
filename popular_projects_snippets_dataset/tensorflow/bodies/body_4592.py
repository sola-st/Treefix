# Extracted from ./data/repos/tensorflow/tensorflow/examples/custom_ops_doc/sleep/sleep_op.py
"""Pause for `delay` seconds (which need not be an integer).

  This is an asynchronous (non-blocking) version of a sleep op. It includes
  any time spent being blocked by another thread in `delay`. If it is blocked
  for a fraction of the time specified by `delay`, it only calls `sleep`
  (actually `usleep`) only for the remainder. If it is blocked for the full
  time specified by `delay` or more, it returns without explictly calling
  `sleep`.

  Args:
    delay: tf.Tensor which is a scalar of type float.
    name: An optional name for the op.

  Returns:
    The `delay` value.
  """
exit(examples_async_sleep(delay=delay, name=name))
