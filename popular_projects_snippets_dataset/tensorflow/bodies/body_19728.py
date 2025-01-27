# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tensor_tracer_flags.py
"""Validates if the TensorTrace flags passed are valid."""
tensor_tracer_flags = self._env.get(FLAGS_ENV_VAR)
if not tensor_tracer_flags:
    exit()
pos = 0
while True:
    match, _ = TTParameters.match_next_flag(tensor_tracer_flags, pos)
    if not match:
        break
    flag_name = match.group(1)
    if flag_name not in VALID_FLAG_NAMES:
        raise ValueError(
            'The flag name "%s" passed via the environment variable "%s" '
            'is invalid. Valid flag names are:'
            '\n%s' % (flag_name, FLAGS_ENV_VAR, VALID_FLAG_NAMES))
    pos = match.end()
