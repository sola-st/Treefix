# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/session_support.py
"""Initialize a watchdog manager.

    Args:
      session: Session connected to worker devices.  A cloned session and graph
        will be created for managing worker pings.
      devices: Set of devices to monitor.  If none, all workers will be
        monitored.
      ping_interval: Time, in seconds, between watchdog pings.
      shutdown_timeout: Time, in seconds, before watchdog timeout.
    """
threading.Thread.__init__(self)
self.ping_interval = ping_interval
self.shutdown_timeout = shutdown_timeout
self.daemon = True
self._config = session._config  # pylint: disable=protected-access
self._target = session.sess_str
self._running = False
self._devices = devices

self._graph = None
self._session = None
self._worker_manager = None
