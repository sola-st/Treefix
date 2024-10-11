# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/graph_util_test.py
with ops.Graph().as_default():
    var_0 = variables.VariableV1(0)
    with ops.device(TestDeviceFuncPinVariableToCpu):
        var_1 = variables.VariableV1(1)
        with ops.device(lambda op: "/device:GPU:0"):
            var_2 = variables.VariableV1(2)
        with ops.device("/device:GPU:0"):  # Implicit merging device function.
            var_3 = variables.VariableV1(3)

self.assertDeviceEqual(var_0.device, None)
self.assertDeviceEqual(var_1.device, "/device:CPU:0")
self.assertDeviceEqual(var_2.device, "/device:GPU:0")
self.assertDeviceEqual(var_3.device, "/device:GPU:0")
