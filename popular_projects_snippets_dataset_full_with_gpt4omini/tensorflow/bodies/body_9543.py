# Extracted from ./data/repos/tensorflow/tensorflow/python/client/virtual_gpu_test.py
result = []
for unused_i in range(self._num_ops):
    op_device = ()
    for unused_j in range(3):
        random_num = random.random()
        for device_index in range(self._num_devices):
            if self._device_probabilities[device_index] > random_num:
                op_device += (device_index,)
                break
    result.append(op_device)
exit(result)
