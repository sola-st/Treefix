# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/config.py
"""Set number of threads used for parallelism between independent operations.

  Determines the number of threads used by independent non-blocking operations.
  0 means the system picks an appropriate number.

  Args:
    num_threads: Number of parallel threads
  """
context.context().inter_op_parallelism_threads = num_threads
