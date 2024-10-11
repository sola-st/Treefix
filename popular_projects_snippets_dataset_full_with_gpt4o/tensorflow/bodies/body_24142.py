# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/wrappers/framework.py
"""Modify a RunOptions object for profiling TensorFlow graph execution.

    Args:
      run_options: (RunOptions) the modified RunOptions object.
    """

run_options.trace_level = config_pb2.RunOptions.FULL_TRACE
