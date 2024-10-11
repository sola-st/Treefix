# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/coordinator/watchdog.py
if os.environ.get("TF_CLUSTER_COORDINATOR_WATCH_DOG_TIMEOUT",
                  "").isnumeric():
    timeout = int(os.environ["TF_CLUSTER_COORDINATOR_WATCH_DOG_TIMEOUT"])
self._timeout = timeout
self._last_activity_time = time.time()
self._traceback_file = traceback_file
self._on_triggered = on_triggered
self._stopped = False
if timeout > 0:
    self._watchdog_thread = threading.Thread(
        target=self._watchdog_function, name="WatchDog", daemon=True)
    self._watchdog_thread.start()
