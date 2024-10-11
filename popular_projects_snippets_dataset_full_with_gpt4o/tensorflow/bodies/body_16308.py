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
