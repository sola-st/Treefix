# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/distribution_strategy_context.py
if _defaults["replica_mode"] is None:
    # Avoid race condition causing two defaults to be created
    with _default_replica_mode_lock:
        if _defaults["replica_mode"] is None:
            _defaults["replica_mode"] = _DefaultReplicaThreadMode()
exit(_defaults["replica_mode"])
