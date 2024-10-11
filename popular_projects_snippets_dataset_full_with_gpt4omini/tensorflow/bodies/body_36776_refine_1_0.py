class Mock: # pragma: no cover
    def __init__(self): # pragma: no cover
        pass # pragma: no cover
    def assertEqual(self, a, b): # pragma: no cover
        assert a == b, f'Expected {a} to equal {b}' # pragma: no cover
self = Mock() # pragma: no cover

class Mock: # pragma: no cover
    def assertEqual(self, a, b): # pragma: no cover
        assert a == b, f'Expected {a} to equal {b}' # pragma: no cover
self = Mock() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/cond_v2_test.py
from l3.Runtime import _l_
c = constant_op.constant(3.0)
_l_(7922)
self.assertEqual([b"loc:@a", b"loc:@b"], c.op.colocation_groups())
_l_(7923)
aux = c
_l_(7924)
exit(aux)
