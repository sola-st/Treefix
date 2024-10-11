# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/session_support.py
"""Reset the graph, session and worker manager."""
self._graph = ops.Graph()
self._session = session_lib.Session(
    target=self._target,
    graph=self._graph,
    config=self._config,
)

if self._devices is None:
    self._devices = all_worker_devices(self._session)

with self._graph.as_default():
    self._worker_manager = WorkerHeartbeatManager.from_devices(
        self._session, self._devices)

if stopping:
    timeout_ms = -1
    shutdown_mode = event_pb2.NOT_CONFIGURED
else:
    timeout_ms = self.shutdown_timeout * 1000
    shutdown_mode = event_pb2.WAIT_FOR_COORDINATOR

self._worker_manager.configure(
    event_pb2.WorkerHeartbeatRequest(
        watchdog_config=event_pb2.WatchdogConfig(timeout_ms=timeout_ms),
        shutdown_mode=shutdown_mode))
