class SelfMock:# pragma: no cover
    def assertEqual(self, a, b):# pragma: no cover
        pass# pragma: no cover
self = SelfMock() # pragma: no cover
def colocation_groups():# pragma: no cover
    return [b"loc:@a", b"loc:@b"]# pragma: no cover
c = type("Mock", (object,), {"op": type("Mock", (object,), {"colocation_groups": colocation_groups})()})() # pragma: no cover

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
