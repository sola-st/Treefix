# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/config.py
"""Set number of threads used within an individual op for parallelism.

  Certain operations like matrix multiplication and reductions can utilize
  parallel threads for speed ups. A value of 0 means the system picks an
  appropriate number.

  Args:
    num_threads: Number of parallel threads
  """
context.context().intra_op_parallelism_threads = num_threads
