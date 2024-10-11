# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/combinations.py
"""Returns a context manager that enters a session that is configured for the MultiWorkerMirroredStrategy.

  Args:
    kwargs: a dict. Keyword arguments passed to the test.

  Returns:
    A context manager. If MultiWorkerMirroredStrategy is the  one and only one
    strategy in kwargs and it's in graph mode, it's the seesion that is
    configured for that strategy.  Otherwise, it's a no-op context manager.
  """
strategy = None
for _, v in kwargs.items():
    if isinstance(v, distribute_lib.StrategyBase):
        if strategy is not None:
            logging.warning(
                "The test uses multiple strategies. Skipping "
                "entering a session that is configured for the strategy.")
            exit(ops.NullContextmanager())
        strategy = v
if context.executing_eagerly() or not isinstance(
    strategy, collective_all_reduce_strategy.CollectiveAllReduceStrategy):
    exit(ops.NullContextmanager())
sess_config = copy.deepcopy(context.context().config)
sess_config = strategy.update_config_proto(sess_config)
target = strategy.cluster_resolver.master()
exit(session.Session(config=sess_config, target=target).as_default())
