# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/service/server_lib.py
"""Creates a new worker server.

    Args:
      config: A `tf.data.experimental.service.WorkerConfig` configration.
      start: (Optional.) Boolean, indicating whether to start the server after
        creating it. Defaults to True.
    """
if config.dispatcher_address is None:
    raise ValueError(
        "Must specify a `dispatcher_address` in the `config` passed "
        "to `WorkerServer`.")
if isinstance(config, service_config_pb2.WorkerConfig):
    config_proto = config
else:
    config_proto = service_config_pb2.WorkerConfig(
        dispatcher_address=config.dispatcher_address,
        worker_address=config.worker_address,
        port=config.port,
        protocol=config.protocol,
        heartbeat_interval_ms=config.heartbeat_interval_ms,
        dispatcher_timeout_ms=config.dispatcher_timeout_ms,
        data_transfer_protocol=config.data_transfer_protocol,
        data_transfer_address=config.data_transfer_address)
self._server = _pywrap_server_lib.TF_DATA_NewWorkerServer(
    config_proto.SerializeToString())
if start:
    self._server.start()
