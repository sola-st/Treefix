import sys # pragma: no cover

class MockOp: # pragma: no cover
    def colocation_groups(self): # pragma: no cover
        return [b"loc:@a", b"loc:@b"] # pragma: no cover
 # pragma: no cover
class MockTensor: # pragma: no cover
    def __init__(self, value): # pragma: no cover
        self.op = MockOp() # pragma: no cover
class MockSelf: # pragma: no cover
    def assertEqual(self, a, b): # pragma: no cover
        print(f"Assertion {'passed' if a == b else 'failed'}: {a} == {b}") # pragma: no cover
self = MockSelf() # pragma: no cover
sys.exit = lambda x: print("Exit called with value:", x) # pragma: no cover

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
