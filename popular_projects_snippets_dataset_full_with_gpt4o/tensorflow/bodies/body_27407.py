# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/service/test_base.py
"""Stops `dispatcher` and creates a new dispatcher with the same port.

    Restarting is supported only when the dispatcher is configured with
    `fault_tolerant_mode=True`.
    """
if not self.dispatcher._config.fault_tolerant_mode:
    raise ValueError(
        "Trying to restart the dispatcher without fault-tolerance.")
port = int(self.dispatcher_address().split(":")[1])
self.dispatcher._stop()
self.dispatcher = server_lib.DispatchServer(
    server_lib.DispatcherConfig(
        port=port,
        work_dir=self.dispatcher._config.work_dir,
        protocol=PROTOCOL,
        fault_tolerant_mode=self.dispatcher._config.fault_tolerant_mode))
