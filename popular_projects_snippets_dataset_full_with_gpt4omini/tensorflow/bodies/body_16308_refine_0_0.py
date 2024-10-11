import numpy as np # pragma: no cover
import mock as ops # pragma: no cover

devices = ['device_1', 'device_2', 'device_3'] # pragma: no cover
nccl_fun = lambda x: x # pragma: no cover
_DeviceTensors = lambda x, y: x # pragma: no cover
tensors = [np.array([1, 2, 3]), np.array([4, 5, 6]), np.array([7, 8, 9])] # pragma: no cover
ops.device = lambda x: contextlib.nullcontext() # pragma: no cover

import numpy as np # pragma: no cover
import mock as ops # pragma: no cover
import contextlib # pragma: no cover

devices = ['device_1', 'device_2', 'device_3'] # pragma: no cover
nccl_fun = lambda x: x # pragma: no cover
_DeviceTensors = lambda x, y: x # pragma: no cover
tensors = [np.array([1, 2, 3]), np.array([4, 5, 6]), np.array([7, 8, 9])] # pragma: no cover
ops.device = lambda x: contextlib.nullcontext() # pragma: no cover

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
