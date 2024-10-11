# Extracted from ./data/repos/tensorflow/tensorflow/python/training/device_setter_test.py
with ops.device(
    device_setter.replica_device_setter(ps_tasks=1, ps_device="/cpu:0")):
    v = variables.Variable([1, 2])
    with ops.device("/job:moon"):
        w = variables.Variable([2, 1])
    a = v + w
    self.assertDeviceEqual("/cpu:0", v.device)
    self.assertDeviceEqual("/cpu:0", v.initializer.device)
    self.assertDeviceEqual("/job:moon/cpu:0", w.device)
    self.assertDeviceEqual("/job:moon/cpu:0", w.initializer.device)
    self.assertDeviceEqual("/job:worker", a.device)
