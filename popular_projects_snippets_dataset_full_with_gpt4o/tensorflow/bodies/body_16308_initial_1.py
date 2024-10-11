import numpy as np # pragma: no cover

devices = ['/device:GPU:0', '/device:GPU:1', '/device:GPU:2'] # pragma: no cover
nccl_fun = lambda x: x # pragma: no cover
tensors = np.array([1, 2, 3, 4, 5]) # pragma: no cover
_DeviceTensors = lambda tensors, devices: {'tensors': tensors, 'devices': devices} # pragma: no cover
ops = type('Mock', (object,), {'device': lambda self, device: self}) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/nccl_ops_test.py
from l3.Runtime import _l_
receiver = np.random.randint(0, len(devices))
_l_(16383)
with ops.device(devices[receiver]):
    _l_(16385)

    aux = [nccl_fun(_DeviceTensors(tensors, devices))]
    _l_(16384)
    exit(aux)
