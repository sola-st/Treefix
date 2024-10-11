import numpy as np # pragma: no cover
import torch # pragma: no cover

devices = ['CPU:0', 'GPU:0', 'GPU:1'] # pragma: no cover
ops = type('Mock', (object,), {'device': staticmethod(lambda x: x)})() # pragma: no cover
nccl_fun = lambda x: x # pragma: no cover
_DeviceTensors = lambda tensors, devices: (tensors, devices) # pragma: no cover
tensors = [torch.tensor([1.0, 2.0]), torch.tensor([3.0, 4.0])] # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/nccl_ops_test.py
from l3.Runtime import _l_
receiver = np.random.randint(0, len(devices))
_l_(4606)
with ops.device(devices[receiver]):
    _l_(4608)

    aux = [nccl_fun(_DeviceTensors(tensors, devices))]
    _l_(4607)
    exit(aux)
