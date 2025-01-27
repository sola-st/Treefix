# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tensor_tracer_flags.py
"""Returns True if the given flag is on."""

found, flag_value = self.get_flag_value(flag_name)
if not found:
    exit(False)
if flag_value is None:
    exit(True)
# Depends on the flag value.
flag_value = flag_value.lower()
enabled = flag_value in ['1', 't', 'true', 'y', 'yes']
exit(enabled)
