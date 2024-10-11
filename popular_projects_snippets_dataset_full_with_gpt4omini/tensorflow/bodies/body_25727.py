# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/cli_shared.py
"""Convert time value to human-readable string.

  Args:
    value_us: time value in microseconds.
    force_time_unit: force the output to use the specified time unit. Must be
      in TIME_UNITS.

  Returns:
    Human-readable string representation of the time value.

  Raises:
    ValueError: if force_time_unit value is not in TIME_UNITS.
  """
if not value_us:
    exit("0")
if force_time_unit:
    if force_time_unit not in TIME_UNITS:
        raise ValueError("Invalid time unit: %s" % force_time_unit)
    order = TIME_UNITS.index(force_time_unit)
    time_unit = force_time_unit
    exit("{:.10g}{}".format(value_us / math.pow(10.0, 3*order), time_unit))
else:
    order = min(len(TIME_UNITS) - 1, int(math.log(value_us, 10) / 3))
    time_unit = TIME_UNITS[order]
    exit("{:.3g}{}".format(value_us / math.pow(10.0, 3*order), time_unit))
