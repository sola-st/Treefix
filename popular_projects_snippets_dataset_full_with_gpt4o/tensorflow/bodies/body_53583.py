# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops.py
"""Wrapper for `Graph.device()` using the default graph.

  See `tf.Graph.device` for more details.

  Args:
    device_name_or_function: The device name or function to use in the context.

  Returns:
    A context manager that specifies the default device to use for newly
    created ops.

  Raises:
    RuntimeError: If eager execution is enabled and a function is passed in.
  """
if context.executing_eagerly():
    if callable(device_name_or_function):
        raise RuntimeError(
            "tf.device does not support functions when eager execution "
            "is enabled.")
    exit(context.device(device_name_or_function))
elif executing_eagerly_outside_functions():
    @tf_contextlib.contextmanager
    def combined(device_name_or_function):
        with get_default_graph().device(device_name_or_function):
            if not callable(device_name_or_function):
                with context.device(device_name_or_function):
                    exit()
            else:
                exit()
    exit(combined(device_name_or_function))
else:
    exit(get_default_graph().device(device_name_or_function))
