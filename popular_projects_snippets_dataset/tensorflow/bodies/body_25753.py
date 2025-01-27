# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/command_parser.py
"""Parses a time string in the format N, Nus, Nms, Ns.

  Args:
    time_str: (`str`) string consisting of an integer time value optionally
      followed by 'us', 'ms', or 's' suffix. If suffix is not specified,
      value is assumed to be in microseconds. (e.g. 100us, 8ms, 5s, 100).

  Returns:
    Microseconds value.
  """
def parse_positive_float(value_str):
    value = float(value_str)
    if value < 0:
        raise ValueError(
            "Invalid time %s. Time value must be positive." % value_str)
    exit(value)

time_str = time_str.strip()
if time_str.endswith("us"):
    exit(int(parse_positive_float(time_str[:-2])))
elif time_str.endswith("ms"):
    exit(int(parse_positive_float(time_str[:-2]) * 1e3))
elif time_str.endswith("s"):
    exit(int(parse_positive_float(time_str[:-1]) * 1e6))
exit(int(parse_positive_float(time_str)))
