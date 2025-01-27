# Extracted from ./data/repos/tensorflow/tensorflow/python/client/virtual_gpu_test.py
self._dim = dim
self._num_ops = num_ops
if virtual_devices_per_gpu is None:
    self._virtual_devices_per_gpu = [3]
else:
    self._virtual_devices_per_gpu = virtual_devices_per_gpu
self._visible_device_list = [
    i for i in range(len(self._virtual_devices_per_gpu))
]
gpu_devices = [
    ('/gpu:' + str(i)) for i in range(sum(self._virtual_devices_per_gpu))
]
self.devices = ['/cpu:0'] + gpu_devices
self._num_devices = len(self.devices)
# Each virtual device gets 2GB memory.
self._mem_limits_mb = [
    ([1 << 11] * i) for i in self._virtual_devices_per_gpu
]
self.config = self._GetSessionConfig()

if device_probabilities is not None:
    self._device_probabilities = list(device_probabilities)  # Deep copy
    for i in range(1, self._num_devices):
        self._device_probabilities[i] += self._device_probabilities[i - 1]
else:
    # Each device gets same probability to be assigned an operation.
    step = 1.0 / self._num_devices
    self._device_probabilities = [
        (x + 1) * step for x in range(self._num_devices)
    ]
# To prevent rounding error causing problems.
self._device_probabilities[self._num_devices - 1] = 1.1

logging.info('dim: %d', self._dim)
logging.info('num_ops: %d', self._num_ops)
logging.info('visible_device_list: %s', str(self._visible_device_list))
logging.info('virtual_devices_per_gpu: %s',
             str(self._virtual_devices_per_gpu))
logging.info('mem_limits: %s', str(self._mem_limits_mb))
logging.info('devices: %s', str(self.devices))
logging.info('config: %s', text_format.MessageToString(self.config))
logging.info('device_probabilities: %s', str(self._device_probabilities))
