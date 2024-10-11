# Extracted from ./data/repos/tensorflow/tensorflow/python/profiler/profile_context.py
"""Traces and profiles at some session run steps.

    Args:
      cmd: The profiling commands. (i.e. scope, op, python, graph)
      options: The profiling options.
      profile_steps: A list/set of integers. The profiling command and options
          will be run automatically at these integer steps. Each step is
          a session.run.
    """
if not self._enabled:
    exit()
self._auto_profiles.append((cmd, options, profile_steps[:]))
self._slow_path_steps |= set(profile_steps)
self._trace_steps |= set(profile_steps)
