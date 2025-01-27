# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/service/test_base.py
"""Restarts the worker, stopping it first if it is already running."""
if self._running:
    self.stop()
port = 0
if use_same_port:
    port = self._port
self._server = _make_worker(self._dispatcher_address,
                            self._data_transfer_protocol,
                            self._shutdown_quiet_period_ms, port)
self._server.start()
self._port = int(self._server._address.split(":")[1])
self._running = True
