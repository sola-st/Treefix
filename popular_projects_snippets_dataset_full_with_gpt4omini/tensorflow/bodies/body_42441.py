# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/core_test.py
with ops.device(self.cpu_device):
    t0 = constant_op.constant(1.0)
    t1 = constant_op.constant(2.0)
self._send(t0, 't0', self.cpu_device)
self._send(t1, 't1', self.cpu_device)
self.assertAllEqual(
    self._recv(dtypes.float32, 't0', self.cpu_device),
    1.0)
self.assertAllEqual(
    self._recv(dtypes.float32, 't1', self.cpu_device),
    2.0)
