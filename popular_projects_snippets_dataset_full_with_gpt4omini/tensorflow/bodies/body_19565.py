# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/session_support.py
"""Shutdown all workers after `shutdown_timeout_secs`."""
logging.info('Shutting down %s.', self)
req = event_pb2.WorkerHeartbeatRequest(
    watchdog_config=event_pb2.WatchdogConfig(timeout_ms=wait_time_in_ms),
    shutdown_mode=event_pb2.SHUTDOWN_AFTER_TIMEOUT,
    exit_code=event_pb2.RequestedExitCode(exit_code=exit_code))
self.configure(req)

# Wait for workers to shutdown.
sleep_sec = 10.0 + wait_time_in_ms / 1000
logging.info('Waiting %.2f seconds for worker shutdown.', sleep_sec)
time.sleep(sleep_sec)
