# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/service/test_base.py
"""Creates a worker server."""
defaults = server_lib.WorkerConfig(dispatcher_address=dispatcher_address)
config_proto = service_config_pb2.WorkerConfig(
    dispatcher_address=dispatcher_address,
    worker_address=defaults.worker_address,
    port=port,
    protocol=PROTOCOL,
    worker_tags=worker_tags,
    heartbeat_interval_ms=TEST_HEARTBEAT_INTERVAL_MS,
    dispatcher_timeout_ms=TEST_DISPATCHER_TIMEOUT_MS,
    data_transfer_protocol=data_transfer_protocol,
    data_transfer_address=defaults.worker_address,
    shutdown_quiet_period_ms=shutdown_quiet_period_ms,
    cross_trainer_cache_size_bytes=cross_trainer_cache_size_bytes)
exit(server_lib.WorkerServer(config_proto, start=False))
