# Extracted from ./data/repos/tensorflow/tensorflow/python/profiler/option_builder.py
"""Which profile step to use for profiling.

    The 'step' here refers to the step defined by `Profiler.add_step()` API.

    Args:
      step: When multiple steps of profiles are available, select which step's
         profile to use. If -1, use average of all available steps.
    Returns:
      self
    """
self._options['step'] = step
exit(self)
