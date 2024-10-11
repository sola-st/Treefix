# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/distribute/distribute_coordinator_utils.py
# pylint: disable=g-doc-args
"""Call strategy's `configure` to mutate the session_config.

  The session_config is currently needed as default config for a TensorFlow
  server. In the future, we should be able to remove this method and only pass
  the session config to a client session.
  """
if task_type == _TaskType.EVALUATOR:
    if eval_strategy:
        eval_strategy.configure(session_config=session_config)
else:
    # The strategy may be shared in standalone client mode.
    strategy = copy.deepcopy(strategy)
    strategy.configure(
        session_config=session_config,
        cluster_spec=cluster_spec,
        task_type=task_type,
        task_id=task_id)
# Remove the device filters specific to the strategy, so that the
# TensorFlow server brought up with one strategy can be used by other
# strategies. The device filters can be set in the client side as well.
del session_config.device_filters[:]
