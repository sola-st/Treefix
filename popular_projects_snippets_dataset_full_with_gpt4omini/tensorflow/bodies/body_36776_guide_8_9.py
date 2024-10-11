class MockOp:  # Mocking the operation class# pragma: no cover
    def colocation_groups(self):# pragma: no cover
        return [b'loc:@a', b'loc:@b'] # pragma: no cover
class MockConstant:# pragma: no cover
    def __init__(self):# pragma: no cover
        self.op = MockOp() # pragma: no cover
def mock_constant(value):  # Mocking the constant function# pragma: no cover
    return MockConstant() # pragma: no cover
self = type('MockSelf', (object,), {'assertEqual': lambda self, a, b: a == b})() # pragma: no cover

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
