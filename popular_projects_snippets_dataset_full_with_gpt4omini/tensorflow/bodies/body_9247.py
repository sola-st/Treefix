# Extracted from ./data/repos/tensorflow/tensorflow/python/profiler/profiler_v2.py
"""Warm-up the profiler session.

  The profiler session will set up profiling context, including loading CUPTI
  library for GPU profiling. This is used for improving the accuracy of
  the profiling results.

  """
start('')
stop(save=False)
