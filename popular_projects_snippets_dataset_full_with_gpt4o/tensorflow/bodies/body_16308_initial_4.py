import numpy as np # pragma: no cover

devices = ['/gpu:0', '/gpu:1', '/gpu:2'] # pragma: no cover
tensors = [np.random.rand(3, 3), np.random.rand(3, 3), np.random.rand(3, 3)] # pragma: no cover
ops = type('MockOps', (object,), {'device': lambda self, x: MockContext(x)})() # pragma: no cover
nccl_fun = lambda x: 'NCCL Operation' # pragma: no cover
_DeviceTensors = lambda tensors, devices: {'tensors': tensors, 'devices': devices} # pragma: no cover
class MockContext:# pragma: no cover
    def __init__(self, device):# pragma: no cover
        self.device = device# pragma: no cover
    def __enter__(self):# pragma: no cover
        return self# pragma: no cover
    def __exit__(self, exc_type, exc_value, traceback):# pragma: no cover
        pass # pragma: no cover

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
