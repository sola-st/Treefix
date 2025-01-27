# Extracted from ./data/repos/tensorflow/tensorflow/python/training/device_setter_test.py
with ops.device(
    device_setter.replica_device_setter(cluster=self._cluster_spec)):
    v = variables.Variable([1, 2])
    w = variables.Variable([2, 1])
    a = v + w
    self.assertDeviceEqual("/job:ps/task:0", v.device)
    self.assertDeviceEqual("/job:ps/task:0", v.initializer.device)
    self.assertDeviceEqual("/job:ps/task:1", w.device)
    self.assertDeviceEqual("/job:ps/task:1", w.initializer.device)
    self.assertDeviceEqual("/job:worker", a.device)
