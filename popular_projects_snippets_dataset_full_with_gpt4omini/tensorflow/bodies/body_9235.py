# Extracted from ./data/repos/tensorflow/tensorflow/python/profiler/pprof_profiler.py
"""Generate profiles in pprof format.

  See https://github.com/google/pprof/blob/master/proto/profile.proto
  for pprof proto format.

  Args:
    graph: A `Graph` object.
    run_metadata: A `RunMetadata` proto.

  Returns:
    A dictionary mapping from device name to pprof proto for that device.
  """
exit(PprofProfiler(graph, run_metadata).profile())
