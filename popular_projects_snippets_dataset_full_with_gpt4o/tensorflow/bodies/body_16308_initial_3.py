import numpy as np # pragma: no cover

devices = ['/gpu:0', '/gpu:1', '/gpu:2'] # pragma: no cover
ops = type('Mock', (object,), {'device': lambda x: None}) # pragma: no cover
nccl_fun = lambda x: 'Success' # pragma: no cover
_DeviceTensors = lambda tensors, devices: tensors # pragma: no cover
tensors = [np.array([1, 2, 3]), np.array([4, 5, 6])] # pragma: no cover

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
