# Extracted from ./data/repos/tensorflow/tensorflow/python/training/device_setter_test.py
with ops.device(
    device_setter.replica_device_setter(cluster=self._cluster_spec)):
    v = variables.Variable([1, 2])
    with ops.device("/job:moon"):
        w = variables.Variable([2, 1])
        with ops.device("/job:ps"):  # Explicit PS job will get task set.
            x = variables.Variable([0, 1])
    a = v + w + x
    self.assertDeviceEqual("/job:ps/task:0", v.device)
    self.assertDeviceEqual("/job:ps/task:0", v.initializer.device)
    self.assertDeviceEqual("/job:moon", w.device)
    self.assertDeviceEqual("/job:moon", w.initializer.device)
    self.assertDeviceEqual("/job:ps/task:1", x.device)
    self.assertDeviceEqual("/job:ps/task:1", x.initializer.device)
    self.assertDeviceEqual("/job:worker", a.device)
