import numpy as np # pragma: no cover
import random # pragma: no cover
import types # pragma: no cover

devices = ['device_0', 'device_1', 'device_2'] # pragma: no cover
ops = type('Mock', (object,), {'device': lambda x: x})() # pragma: no cover
nccl_fun = lambda x: x # pragma: no cover
_DeviceTensors = lambda x, y: x # pragma: no cover
tensors = [np.random.rand(3, 3) for _ in range(len(devices))] # pragma: no cover

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
