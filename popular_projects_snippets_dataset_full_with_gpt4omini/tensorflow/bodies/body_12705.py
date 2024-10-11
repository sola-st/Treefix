# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/critical_section_ops.py
"""Creates a critical section."""
context.ensure_initialized()
if critical_section_def and name is not None:
    raise ValueError(f"Arguments critical_section_def={critical_section_def} "
                     f"and shared_name={shared_name} are mutually exclusive. "
                     "Please only specify one of them.")
if critical_section_def:
    raise ValueError("Argument `critical_section_def` is not supported.")
else:
    self._init_from_args(name, shared_name)
