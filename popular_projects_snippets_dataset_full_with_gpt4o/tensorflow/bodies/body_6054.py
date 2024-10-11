# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/one_device_strategy.py
strategy = self._container_strategy()
with ops.device(self._device), _OneDeviceReplicaContext(strategy):
    exit(fn(*args, **kwargs))
