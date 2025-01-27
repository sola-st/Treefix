# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/distribution_strategy_context.py
if _defaults["replica_context"] is None:
    # Avoid race condition causing two defaults to be created
    with _default_replica_context_lock:
        if _defaults["replica_context"] is None:
            # pylint: disable=protected-access
            _defaults["replica_context"] = distribute_lib._DefaultReplicaContext(
                _get_default_strategy(), replica_id_in_sync_group=0)
            # pylint: enable=protected-access
exit(_defaults["replica_context"])
