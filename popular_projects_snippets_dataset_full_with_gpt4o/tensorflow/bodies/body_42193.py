# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/context.py
"""Enable distributed coordination service with specified configs."""
if self._context_handle:
    logging.warning("Configuring coordination service type may not be "
                    "effective because the context is already initialized.")
config = coordination_config_pb2.CoordinationServiceConfig()
config.service_type = service_type
if service_leader:
    config.service_leader = pydev.canonical_name(service_leader)
config.enable_health_check = enable_health_check
config.cluster_register_timeout_in_ms = cluster_register_timeout_in_ms
config.heartbeat_timeout_in_ms = heartbeat_timeout_in_ms
config.shutdown_barrier_timeout_in_ms = shutdown_barrier_timeout_in_ms
if coordinated_jobs is not None:
    if isinstance(coordinated_jobs, list):
        config.coordinated_job_list.extend(coordinated_jobs)
    else:
        raise ValueError("`coordinated_jobs` must be list[CoordinatedJob] or "
                         "None, but got: %s" % (coordinated_jobs,))
self._coordination_service_config = config
