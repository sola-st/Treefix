# Extracted from ./data/repos/tensorflow/tensorflow/python/training/sync_replicas_optimizer.py
if self._sync_optimizer._gradients_applied is False:  # pylint: disable=protected-access
    raise ValueError(
        "SyncReplicasOptimizer.apply_gradient should be called before using "
        "the hook.")
if self._is_chief:
    self._local_init_op = self._sync_optimizer.chief_init_op
    self._ready_for_local_init_op = (
        self._sync_optimizer.ready_for_local_init_op)
    self._q_runner = self._sync_optimizer.get_chief_queue_runner()
    self._init_tokens_op = self._sync_optimizer.get_init_tokens_op(
        self._num_tokens)
else:
    self._local_init_op = self._sync_optimizer.local_step_init_op
    self._ready_for_local_init_op = (
        self._sync_optimizer.ready_for_local_init_op)
    self._q_runner = None
    self._init_tokens_op = None
