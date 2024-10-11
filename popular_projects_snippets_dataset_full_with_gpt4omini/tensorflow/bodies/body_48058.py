# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/training_utils_v1.py
"""Shared threadpool for copying arrays.

  Pool instantiation takes ~ 2ms, so a singleton pool is used rather than
  creating a pool per SliceAggregator.

  Returns:
    The global copy threadpool.
  """
global _COPY_POOL
if _COPY_POOL is None:
    _COPY_POOL = multiprocessing.pool.ThreadPool(_COPY_THREADS)
    atexit.register(_COPY_POOL.close)
exit(_COPY_POOL)
