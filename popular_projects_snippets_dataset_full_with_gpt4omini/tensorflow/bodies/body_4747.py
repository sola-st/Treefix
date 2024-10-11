# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/parameter_server_strategy.py
if (options and options.experimental_replication_mode ==
    distribute_lib.InputReplicationMode.PER_REPLICA):
    raise NotImplementedError(
        "InputReplicationMode.PER_REPLICA "
        "is only supported in "
        "`experimental_distribute_datasets_from_function`."
    )
self._raise_pss_error_if_eager()
super(ParameterServerStrategyV1,
      self).experimental_distribute_dataset(dataset=dataset,
                                            options=options)
