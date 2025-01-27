# Extracted from ./data/repos/tensorflow/tensorflow/python/training/device_setter_test.py
cluster_spec = server_lib.ClusterSpec({
    "sun": ["sun0:2222", "sun1:2222", "sun2:2222"],
    "moon": ["moon0:2222", "moon1:2222"]
})

with ops.device(
    device_setter.replica_device_setter(
        ps_device="/job:moon/cpu:0",
        worker_device="/job:sun",
        cluster=cluster_spec.as_cluster_def())):
    v = variables.Variable([1, 2])
    w = variables.Variable([2, 1])
    a = v + w
    self.assertDeviceEqual("/job:moon/task:0/cpu:0", v.device)
    self.assertDeviceEqual("/job:moon/task:0/cpu:0", v.initializer.device)
    self.assertDeviceEqual("/job:moon/task:1/cpu:0", w.device)
    self.assertDeviceEqual("/job:moon/task:1/cpu:0", w.initializer.device)
    self.assertDeviceEqual("/job:sun", a.device)
