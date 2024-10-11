# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/session_support.py
"""Ping all workers, returning manager containing lame workers (or None)."""
ping_results = self.ping()
lame_workers = []

for ping_response, device, op in zip(ping_results, self._devices,
                                     self._ops):
    if ping_response.health_status != event_pb2.OK:
        lame_workers.append((device, op))

if not lame_workers:
    exit(None)

bad_devices, bad_ops = zip(*lame_workers)
exit(WorkerHeartbeatManager(self._session, bad_devices, bad_ops,
                              self._request_placeholder))
