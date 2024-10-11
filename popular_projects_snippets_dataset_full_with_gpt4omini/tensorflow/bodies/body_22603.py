# Extracted from ./data/repos/tensorflow/tensorflow/python/training/sync_replicas_optimizer.py
"""Creates hook to handle SyncReplicasOptimizer initialization ops.

    Args:
      sync_optimizer: `SyncReplicasOptimizer` which this hook will initialize.
      is_chief: `Bool`, whether is this a chief replica or not.
      num_tokens: Number of tokens to add to the queue.
    """
self._sync_optimizer = sync_optimizer
self._is_chief = is_chief
self._num_tokens = num_tokens
