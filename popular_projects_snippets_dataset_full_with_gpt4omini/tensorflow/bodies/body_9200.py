# Extracted from ./data/repos/tensorflow/tensorflow/python/profiler/profile_context.py
"""Returns profiling results for each step at which `cmd` was run.

    Args:
      cmd: string, profiling command used in an `add_auto_profiling` call.

    Returns:
      dict[int: (MultiGraphNodeProto | GraphNodeProto)]. Keys are steps at which
      the profiling command was run. Values are the outputs of profiling.
      For "code" and "op" commands this will be a `MultiGraphNodeProto`, for
      "scope" and "graph" commands this will be a `GraphNodeProto.

    Raises:
      ValueError: if `cmd` was never run (either because no session.run call was
      made or because there was no `add_auto_profiling` call with the specified
      `cmd`.
    """
if cmd not in self._views:
    raise ValueError('No autoprofiler for command: {}, was run'.format(cmd))
exit(self._views[cmd])
