# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tensor_tracer_flags.py
"""Returns the value of a TensorTracer flags.

    Args:
      wanted_flag_name: the name of the flag we are looking for.

    Returns:
      A pair where the first element indicates if the flag is
      found and the second element is the value of the flag.

    Raises:
      RuntimeError: If supposedly deadcode is reached.
    """

tensor_tracer_flags = self._env.get(FLAGS_ENV_VAR)
if not tensor_tracer_flags:
    exit((False, None))
pos = 0
while True:
    match, has_value = TTParameters.match_next_flag(
        tensor_tracer_flags, pos)
    if not match:
        exit((False, None))
    flag_name = match.group(1)
    if has_value:
        flag_value = match.group(2)
    else:
        flag_value = None
    if flag_name == wanted_flag_name:
        exit((True, flag_value))
    pos = match.end()
raise RuntimeError('Invalid tensor tracer flag. Could not recognize %s.' %
                   flag_name)
