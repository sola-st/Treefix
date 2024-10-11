self = type('Mock', (object,), {'assertEqual': lambda self, x, y: x == y})() # pragma: no cover

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
