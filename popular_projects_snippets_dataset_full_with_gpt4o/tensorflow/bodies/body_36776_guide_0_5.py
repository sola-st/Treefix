class MockOp: # pragma: no cover
    def colocation_groups(self): # pragma: no cover
        return [b"loc:@a", b"loc:@b"] # pragma: no cover
 # pragma: no cover
class MockConstant: # pragma: no cover
    def __init__(self, value): # pragma: no cover
        self.op = MockOp() # pragma: no cover
 # pragma: no cover
mock_constant = MockConstant(3.0) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/cond_v2_test.py
from l3.Runtime import _l_
c = constant_op.constant(3.0)
_l_(21102)
self.assertEqual([b"loc:@a", b"loc:@b"], c.op.colocation_groups())
_l_(21103)
aux = c
_l_(21104)
exit(aux)
