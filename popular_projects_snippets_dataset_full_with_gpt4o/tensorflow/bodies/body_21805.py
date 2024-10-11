# Extracted from ./data/repos/tensorflow/tensorflow/python/training/device_setter_test.py
with ops.device(
    device_setter.replica_device_setter(cluster=self._cluster_spec)):
    v = resource_variable_ops.ResourceVariable([1, 2])
    self.assertDeviceEqual("/job:ps/task:0", v.device)
