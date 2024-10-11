# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/preempted_hook.py
if tpu_cluster_resolver.is_running_in_gce():
    self._tpu_poller = _TPUPollingThread(self._cluster, session)
    self._tpu_poller.start()
