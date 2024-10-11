constant_op = type('Mock', (object,), {'constant': lambda x: type('MockTensor', (object,), {'op': type('MockOp', (object,), {'colocation_groups': lambda: [b'loc:@a', b'loc:@b']})()})()}) # pragma: no cover
self = type('MockSelf', (object,), {'assertEqual': lambda self, a, b: print(f'Assertion passed: {a} == {b}' if a == b else f'Assertion failed: {a} != {b}')})() # pragma: no cover

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
