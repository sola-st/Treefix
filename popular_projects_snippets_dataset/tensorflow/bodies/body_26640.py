# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/service/server_lib.py
"""Creates a new dispatch server.

    Args:
      config: (Optional.) A `tf.data.experimental.service.DispatcherConfig`
        configration. If `None`, the dispatcher will use default
        configuration values.
      start: (Optional.) Boolean, indicating whether to start the server after
        creating it. Defaults to True.
    """
config = config or DispatcherConfig()
if config.fault_tolerant_mode and not config.work_dir:
    raise ValueError(
        "Cannot enable fault tolerant mode without configuring a work dir. "
        "Make sure to set `work_dir` in the `config` object passed to "
        "`DispatcherServer`.")
self._config = config
if isinstance(config, service_config_pb2.DispatcherConfig):
    config_proto = config
else:
    config_proto = service_config_pb2.DispatcherConfig(
        port=config.port,
        protocol=config.protocol,
        work_dir=config.work_dir,
        fault_tolerant_mode=config.fault_tolerant_mode,
        worker_addresses=config.worker_addresses,
        job_gc_check_interval_ms=config.job_gc_check_interval_ms,
        job_gc_timeout_ms=config.job_gc_timeout_ms)
self._server = _pywrap_server_lib.TF_DATA_NewDispatchServer(
    config_proto.SerializeToString())
if start:
    self._server.start()
