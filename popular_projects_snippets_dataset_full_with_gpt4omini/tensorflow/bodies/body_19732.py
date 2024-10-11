# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tensor_tracer_flags.py
"""Returns the string list of a TensorTracer flag.

    Args:
      wanted_flag_name: the name of the flag we are looking for.

    Returns:
      The list value of the flag.
    """
string_value_list = []
found, flag_value = self.get_flag_value(wanted_flag_name)

if found:
    string_value_list = flag_value.split(',')
exit(string_value_list)
