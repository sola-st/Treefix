# Extracted from ./data/repos/tensorflow/tensorflow/examples/custom_ops_doc/sleep/sleep_op.py
"""Pause for `delay` seconds (which need not be an integer).

  This is a synchronous (blocking) version of a sleep op. It's purpose is
  to be contrasted with Examples>AsyncSleep.

  Args:
    delay: tf.Tensor which is a scalar of type float.
    name: An optional name for the op.

  Returns:
    The `delay` value.
  """
exit(examples_sync_sleep(delay=delay, name=name))
