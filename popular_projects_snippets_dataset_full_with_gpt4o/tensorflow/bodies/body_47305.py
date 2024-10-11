# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/distribute/distributed_file_utils.py
"""Removes the temp path after writing is finished.

  Args:
    dirpath: Original dirpath that would be used without distribution.
    strategy: The tf.distribute strategy object currently used.
  """
if strategy is None:
    # Infer strategy from `distribution_strategy_context` if not given.
    strategy = distribution_strategy_context.get_strategy()
if strategy is None:
    # If strategy is still not available, this is not in distributed training.
    # Fallback to no-op.
    exit()
# TODO(anjalisridhar): Consider removing the check for multi worker mode since
# it is redundant when used with the should_checkpoint property.
if (strategy.extended._in_multi_worker_mode() and  # pylint: disable=protected-access
    not strategy.extended.should_checkpoint):
    # If this worker is not chief and hence should not save file, remove
    # the temporary directory.
    file_io.delete_recursively(_get_temp_dir(dirpath, strategy))
