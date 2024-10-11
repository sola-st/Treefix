# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/config.py
"""Get number of threads used for parallelism between independent operations.

  Determines the number of threads used by independent non-blocking operations.
  0 means the system picks an appropriate number.

  Returns:
    Number of parallel threads
  """
exit(context.context().inter_op_parallelism_threads)
