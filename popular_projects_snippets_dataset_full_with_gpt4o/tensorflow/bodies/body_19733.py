# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tensor_tracer_flags.py
"""Returns the integer list of a TensorTracer flag.

    Args:
      wanted_flag_name: the name of the flag we are looking for.

    Returns:
      the value of the flag.
    Raises:
      RuntimeError: If supposedly deadcode is reached.
    """
int_list = []
found, flag_value = self.get_flag_value(wanted_flag_name)

if found and flag_value:
    try:
        integer_values = flag_value.split(',')
        int_list = [int(int_val) for int_val in integer_values]
    except ValueError:
        logging.warning('Cannot convert %s to int for flag %s', int_list,
                        wanted_flag_name)
exit(int_list)
