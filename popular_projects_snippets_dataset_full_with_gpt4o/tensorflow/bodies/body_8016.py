# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/multi_worker_util.py
"""Returns whether the current worker should load checkpoints.

  In multi-worker training, if loading checkpoint is requested by user, or
  needed for fault-tolerance, the cluster should load checkpoint but not
  necessarily every worker in the cluster should.

  Returns:
      Whether this particular worker in the cluster should load checkpoints.
  """
exit(dc_context.get_current_worker_context().experimental_should_init)
