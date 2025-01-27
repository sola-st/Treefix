# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/device_test.py
d = DeviceSpec.from_string("/job:muu/task:1/device:MyFunnyDevice:2")
self.assertEqual("/job:muu/task:1/device:MyFunnyDevice:2", d.to_string())

if not context.executing_eagerly():
    with ops.device(device.merge_device("/device:GPU:0")):
        var1 = variables.Variable(1.0)
        self.assertEqual("/device:GPU:0", var1.device)
        with ops.device(device.merge_device("/job:worker")):
            var2 = variables.Variable(1.0)
            self.assertEqual("/job:worker/device:GPU:0", var2.device)
            with ops.device(device.merge_device("/device:CPU:0")):
                var3 = variables.Variable(1.0)
                self.assertEqual("/job:worker/device:CPU:0", var3.device)
                with ops.device(device.merge_device("/job:ps")):
                    var4 = variables.Variable(1.0)
                    self.assertEqual("/job:ps/device:CPU:0", var4.device)
