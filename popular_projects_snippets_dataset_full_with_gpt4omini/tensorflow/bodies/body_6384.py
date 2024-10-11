# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/collective_all_reduce_strategy.py
# CollectiveAllReduce works on a predefined set of devices. In most cases
# they should be the compute devices, but certain use cases may reduce host
# tensors as well (e.g. early stopping). We infer the cross_device_ops to
# use based on the number of devices, since inputs don't always have device
# annotations. The compute devices one is preferred since we can potentially
# leverage NCCL.
if isinstance(value, values.DistributedValues):
    num_devices = len(value._values)  # pylint: disable=protected-access
else:
    num_devices = 1
if num_devices == len(self.worker_devices):
    exit(self._cross_device_ops)
else:
    exit(self._host_cross_device_ops)
