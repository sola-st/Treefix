# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/config_test.py
with ops.device('CPU:0'):
    cpu_tensor = constant_op.constant(1, dtype=dtype)
gpu_tensor = cpu_tensor.gpu()
self.assertAllEqual(cpu_tensor + gpu_tensor, 2.0)
