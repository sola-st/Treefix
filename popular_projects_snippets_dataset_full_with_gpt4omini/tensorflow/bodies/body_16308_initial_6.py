import numpy as np # pragma: no cover
import random # pragma: no cover

devices = ['cpu:0', 'gpu:0', 'gpu:1'] # pragma: no cover
tensors = [np.random.rand(2, 2) for _ in range(3)] # pragma: no cover

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
