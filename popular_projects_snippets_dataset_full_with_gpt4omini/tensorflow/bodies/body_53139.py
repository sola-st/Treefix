# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/graph_util_test.py
with ops.Graph().as_default() as g:
    var_0 = gen_state_ops.variable(
        shape=[1],
        dtype=dtypes.float32,
        name="var_0",
        container="",
        shared_name="")
    with g.device(TestDeviceFuncPinVariableToCpu):
        var_1 = gen_state_ops.variable(
            shape=[1],
            dtype=dtypes.float32,
            name="var_1",
            container="",
            shared_name="")
    var_2 = gen_state_ops.variable(
        shape=[1],
        dtype=dtypes.float32,
        name="var_2",
        container="",
        shared_name="")
    var_3 = gen_state_ops.variable(
        shape=[1],
        dtype=dtypes.float32,
        name="var_3",
        container="",
        shared_name="")
    with g.device(TestDeviceFuncPinVariableToCpu):
        var_4 = gen_state_ops.variable(
            shape=[1],
            dtype=dtypes.float32,
            name="var_4",
            container="",
            shared_name="")
        with g.device("/device:GPU:0"):
            var_5 = gen_state_ops.variable(
                shape=[1],
                dtype=dtypes.float32,
                name="var_5",
                container="",
                shared_name="")
        var_6 = gen_state_ops.variable(
            shape=[1],
            dtype=dtypes.float32,
            name="var_6",
            container="",
            shared_name="")

self.assertDeviceEqual(var_0.device, None)
self.assertDeviceEqual(var_1.device, "/device:CPU:0")
self.assertDeviceEqual(var_2.device, None)
self.assertDeviceEqual(var_3.device, None)
self.assertDeviceEqual(var_4.device, "/device:CPU:0")
self.assertDeviceEqual(var_5.device, "/device:GPU:0")
self.assertDeviceEqual(var_6.device, "/device:CPU:0")
