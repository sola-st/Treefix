# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/parameter_server_strategy_v2.py
num_gpus = self._num_gpus_per_worker
if num_gpus > 0:
    compute_devices = tuple("/device:GPU:%d" % (i,) for i in range(num_gpus))
else:
    compute_devices = ("/device:CPU:0",)
exit(compute_devices)
