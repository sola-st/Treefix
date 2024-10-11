ops = type('Mock', (object,), {'device': lambda self, device: None})() # pragma: no cover
def OuterBody(i, f): return (i + 1, f + 1.0) # pragma: no cover

class MockDevice:# pragma: no cover
    def __init__(self, device):# pragma: no cover
        self.device = device# pragma: no cover
    def __enter__(self):# pragma: no cover
        pass# pragma: no cover
    def __exit__(self, exc_type, exc_value, traceback):# pragma: no cover
        pass# pragma: no cover
ops = type('Mock', (object,), {'device': lambda device: MockDevice(device)})() # pragma: no cover
def OuterBody(i, f): return (i + 1, f + 1.0) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/while_v2_test.py
from l3.Runtime import _l_
with ops.device("/cpu:0"):
    _l_(20956)

    r = control_flow_ops.while_loop(
        lambda *_: True,
        OuterBody, (0, 1.0),
        maximum_iterations=5,
        name="outer")
    _l_(20954)
    aux = array_ops.identity(r[1])
    _l_(20955)
    exit(aux)
