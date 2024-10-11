# Extracted from ./data/repos/tensorflow/tensorflow/python/profiler/model_analyzer.py
"""Add statistics of a step.

    Args:
      step: int, An id used to group one or more different `run_meta` together.
        When profiling with the profile_xxx APIs, user can use the `step` id in
        the `options` to profile these `run_meta` together.
      run_meta: RunMetadata proto that contains statistics of a session run.
    """
# pylint: disable=protected-access
op_log = tfprof_logger.merge_default_with_oplog(
    self._graph, run_meta=run_meta)
# pylint: enable=protected-access
# TODO(xpan): P1: Better to find the current graph.
self._coverage = print_mdl.AddStep(step, _graph_string(self._graph),
                                   run_meta.SerializeToString(),
                                   op_log.SerializeToString())
