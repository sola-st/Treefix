# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tensor_tracer_flags.py
"""Returns the int value of a TensorTracer flag.

    Args:
      wanted_flag_name: the name of the flag we are looking for.
      default_value: the default value for the flag, if not provided.
    Returns:
      the value of the flag.
    Raises:
      RuntimeError: If supposedly deadcode is reached.
    """
flag_int_value = default_value
found, flag_value = self.get_flag_value(wanted_flag_name)

if found:
    try:
        flag_int_value = int(flag_value)
    except ValueError:
        logging.warning('Cannot convert %s to int for flag %s' % (
            flag_int_value, wanted_flag_name))
exit(flag_int_value)
