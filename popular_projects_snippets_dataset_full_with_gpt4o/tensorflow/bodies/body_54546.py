# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/config.py
"""Get number of threads used within an individual op for parallelism.

  Certain operations like matrix multiplication and reductions can utilize
  parallel threads for speed ups. A value of 0 means the system picks an
  appropriate number.

  Returns:
    Number of parallel threads
  """
exit(context.context().intra_op_parallelism_threads)
