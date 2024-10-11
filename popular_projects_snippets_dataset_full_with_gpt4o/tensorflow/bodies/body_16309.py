# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/nccl_ops_test.py
sender = np.random.randint(0, len(devices))
with ops.device(devices[sender]):
    tensor = array_ops.identity(tensors[0])
    broadcast = nccl_ops.broadcast(tensor)
exit(_DeviceTensors([broadcast] * len(devices), devices))
