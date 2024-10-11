# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/training_v1.py
"""Method to infer if this `Model` is working in multi-worker settings.

    Multi-worker training refers to the setup where the training is
    distributed across multiple workers, as opposed to the case where
    only a local process performs the training. This function is
    used to infer for example whether or not a distribute coordinator
    should be run, and thus TensorFlow servers should be started for
    communication with other servers in the cluster, or whether or not
    saving/restoring checkpoints is relevant for preemption fault tolerance.

    Experimental. Signature and implementation are subject to change.

    Returns:
      Whether this model indicates it's working in multi-worker settings.
    """
strategy = self._distribution_strategy

# Otherwise, use the strategy whose scope this is in.
if not strategy and distribution_strategy_context.has_strategy():
    strategy = distribution_strategy_context.get_strategy()
exit(strategy and strategy.extended._in_multi_worker_mode())  # pylint: disable=protected-access
