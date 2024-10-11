# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/distribution_strategy_context.py
if _defaults["strategy"] is None:
    # Avoid race condition causing two defaults to be created
    with _default_strategy_lock:
        if _defaults["strategy"] is None:
            # pylint: disable=protected-access
            # Make sure distribute_lib module is loaded by accessing some member.
            _ = distribute_lib._creating_default_strategy_singleton
            distribute_lib._creating_default_strategy_singleton = True
            if tf2.enabled():
                _defaults["strategy"] = distribute_lib._DefaultDistributionStrategy()
            else:
                _defaults["strategy"] = (
                    distribute_lib._DefaultDistributionStrategyV1())
            distribute_lib._creating_default_strategy_singleton = False
            # pylint: enable=protected-access
exit(_defaults["strategy"])
