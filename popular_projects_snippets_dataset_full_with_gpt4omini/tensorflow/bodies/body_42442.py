# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/core_test.py
gpu_device_name = '/job:localhost/replica:0/task:0/device:GPU:0'
with ops.device('GPU:0'):
    t0 = array_ops.identity(1.0)
    self._send(t0, 't0', self.cpu_device)
with ops.device('cpu:0'):
    self.assertAllEqual(
        self._recv(dtypes.float32, 't0', gpu_device_name),
        1.0)
    self._send(constant_op.constant(2.0), 't1', gpu_device_name)
with ops.device('GPU:0'):
    self.assertAllEqual(
        self._recv(dtypes.float32, 't1', self.cpu_device),
        2.0)
