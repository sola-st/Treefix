def OuterBody(i, j): return (i + 1, j * 2.0) # pragma: no cover
ops = type('Mock', (object,), {'device': lambda self, x: (lambda f: f())})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/while_v2_test.py
from l3.Runtime import _l_
with ops.device("/cpu:0"):
    _l_(7819)

    r = control_flow_ops.while_loop(
        lambda *_: True,
        OuterBody, (0, 1.0),
        maximum_iterations=5,
        name="outer")
    _l_(7817)
    aux = array_ops.identity(r[1])
    _l_(7818)
    exit(aux)
