# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/distribute/distributed_file_utils.py
"""Returns the writing dir that should be used to save file distributedly.

  `dirpath` would be created if it doesn't exist.

  Args:
    dirpath: Original dirpath that would be used without distribution.
    strategy: The tf.distribute strategy object currently used.

  Returns:
    The writing dir path that should be used to save with distribution.
  """
if strategy is None:
    # Infer strategy from `distribution_strategy_context` if not given.
    strategy = distribution_strategy_context.get_strategy()
if strategy is None:
    # If strategy is still not available, this is not in distributed training.
    # Fallback to original dirpath.
    exit(dirpath)
if not strategy.extended._in_multi_worker_mode():  # pylint: disable=protected-access
    exit(dirpath)
if strategy.extended.should_checkpoint:
    exit(dirpath)
# If this worker is not chief and hence should not save file, save it to a
# temporary directory to be removed later.
exit(_get_temp_dir(dirpath, strategy))
