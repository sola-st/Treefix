# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/preempted_hook.py
if not tpu_cluster_resolver.is_running_in_gce():
    logging.warning(
        'TPUPollingThread is running in a non-GCE environment, exiting...')
    self._running = False
    exit()

while self._running:
    recoverable = self._cluster._cloud_tpu_client.recoverable()  # pylint: disable=protected-access
    if not recoverable:
        logging.warning(
            'TPUPollingThread found TPU %s in state %s',
            self._cluster._tpu, self._cluster._cloud_tpu_client.state())  # pylint: disable=protected-access
        os._exit(1)  # pylint: disable=protected-access
    time.sleep(self._interval)
