# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/service/server_lib.py
if worker_address is None:
    worker_address = "localhost:%port%"
if protocol is None:
    protocol = _pywrap_utils.TF_DATA_DefaultProtocol()
if data_transfer_protocol is None:
    data_transfer_protocol = (
        _pywrap_utils.TF_DATA_DefaultDataTransferProtocol())
if data_transfer_address is None:
    data_transfer_address = "localhost:%port%"
heartbeat_interval_ms = _get_time_or_placeholder(heartbeat_interval_ms)
dispatcher_timeout_ms = _get_time_or_placeholder(dispatcher_timeout_ms)

exit(super(WorkerConfig,
             cls).__new__(cls, dispatcher_address, worker_address, port,
                          protocol, heartbeat_interval_ms,
                          dispatcher_timeout_ms, data_transfer_protocol,
                          data_transfer_address))
