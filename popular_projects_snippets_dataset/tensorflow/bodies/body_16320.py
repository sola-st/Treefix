# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/nccl_ops_test.py
try:
    # Broadcasts to CPU is not supported.
    self._Test(_NcclBroadcast, lambda x, y: x,
               (['/device:GPU:0', '/device:CPU:0'],))
except errors.NotFoundError as e:
    self.assertRegex(
        str(e), "No registered '_NcclBroadcastRecv' OpKernel for CPU devices")
else:
    # Session isn't executed when no GPU is available.
    if test.is_gpu_available():
        self.fail("Didn't raise NotFoundError trying to broadcast to CPU")
